#!/usr/bin/env python3
"""Fetch citation identities; report mismatches without rewriting the bibliography.

Requires bibtexparser==1.4.3. Network failures are NOT evidence of fabrication.
Title/author matching is a screening step, not verification of an attributed claim.
Raw public responses are cached with hashes for manual inspection.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import threading
import time
import unicodedata
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

import bibtexparser
from bibtexparser.customization import convert_to_unicode


ROOT = Path(__file__).resolve().parents[1]
ARXIV_LOCK = threading.Lock()
LAST_ARXIV = 0.0


class CitationMeta(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.values = {}

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta" and attrs.get("name", "").startswith("citation_"):
            self.values.setdefault(attrs["name"], []).append(attrs.get("content", ""))


def normalize(text):
    text = unicodedata.normalize("NFKD", str(text)).casefold()
    return re.sub(r"[^a-z0-9]", "", text)


def author_tokens(name):
    # Word order differs across publishers; retain every normalized name token.
    name = unicodedata.normalize("NFKD", name).casefold()
    name = "".join(c for c in name if not unicodedata.combining(c))
    return sorted(re.findall(r"[a-z0-9]+", name))


def fetch(url, out, refresh=False):
    global LAST_ARXIV
    key = hashlib.sha256(url.encode()).hexdigest()
    cache = out / "responses" / (key + ".json")
    if cache.exists() and not refresh:
        return json.loads(cache.read_text())
    if url.startswith("https://arxiv.org/"):
        with ARXIV_LOCK:
            time.sleep(max(0, 3.1 - (time.monotonic() - LAST_ARXIV)))
            LAST_ARXIV = time.monotonic()
    record = {"url": url, "retrieved_at": datetime.now(timezone.utc).isoformat()}
    try:
        request = Request(url, headers={"User-Agent": "ManuscriptCitationAudit/1.0"})
        with urlopen(request, timeout=20) as response:
            body = response.read()
            record.update(status=response.status, final_url=response.url,
                          sha256=hashlib.sha256(body).hexdigest(),
                          body=body.decode("utf-8", errors="replace"))
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        record.update(status=getattr(exc, "code", None), error=str(exc))
    cache.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n")
    return record


def extract(kind, body):
    if kind == "crossref":
        item = json.loads(body)["message"]
        date = item.get("published", item.get("issued", {})).get("date-parts", [[]])[0]
        return {
            "title": item.get("title", [""])[0],
            "authors": [" ".join((a.get("given", ""), a.get("family", ""))).strip()
                        for a in item.get("author", [])],
            "year": str(date[0]) if date else "",
            "venue": item.get("container-title", []),
            "pages": item.get("page", ""), "volume": item.get("volume", ""),
            "doi": item.get("DOI", ""),
        }
    if kind == "datacite":
        item = json.loads(body)["data"]["attributes"]
        return {"title": item["titles"][0]["title"],
                "authors": [a["name"] for a in item.get("creators", [])],
                "year": str(item.get("publicationYear", "")),
                "doi": item.get("doi", ""),
                "related_identifiers": item.get("relatedIdentifiers", [])}
    parser = CitationMeta()
    parser.feed(body)
    meta = parser.values
    result = {"title": meta.get("citation_title", [""])[0],
              "authors": meta.get("citation_author", []),
              "date": meta.get("citation_date", [])}
    # Keep venue comments for manual review; do not infer acceptance from keywords.
    for field in ("comments", "journal-ref"):
        match = re.search(r'<td[^>]*class="[^"]*' + field + r'[^\"]*"[^>]*>(.*?)</td>', body, re.S)
        if match:
            result[field] = re.sub(r"<[^>]+>", " ", match.group(1)).strip()
    return result


def audit(entry, provenance, out, refresh):
    urls = []
    if entry.get("doi"):
        urls.append(("crossref", "https://api.crossref.org/works/" + entry["doi"]))
    arxiv_id = provenance.get("arxiv_id")
    if arxiv_id:
        urls.append(("arxiv", "https://arxiv.org/abs/" + arxiv_id))
        if not entry.get("doi"):
            urls.append(("datacite", "https://api.datacite.org/dois/10.48550/arxiv." + arxiv_id))
    result = {"key": entry["ID"], "bibliography": entry, "sources": []}
    for kind, url in urls:
        raw = fetch(url, out, refresh)
        source = {k: v for k, v in raw.items() if k != "body"}
        source["kind"] = kind
        if "body" in raw:
            try:
                data = extract(kind, raw["body"])
                source["metadata"] = data
                source["title_matches"] = normalize(data["title"]) == normalize(entry["title"])
                source["authors_match"] = (
                    [author_tokens(a) for a in data["authors"]]
                    == [author_tokens(a) for a in entry["author"].split(" and ")]
                )
                if kind == "crossref":
                    source["year_matches"] = data["year"] == entry["year"]
                    source["pages_match"] = normalize(data["pages"]) == normalize(entry.get("pages", ""))
            except (ValueError, KeyError, TypeError, IndexError) as exc:
                source["parse_error"] = str(exc)
        result["sources"].append(source)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=ROOT / "build/citation-audit")
    parser.add_argument("--refresh", action="store_true")
    args = parser.parse_args()
    (args.out / "responses").mkdir(parents=True, exist_ok=True)
    database = bibtexparser.loads((ROOT / "references.bib").read_text())
    entries = [convert_to_unicode(dict(item)) for item in database.entries]
    provenance = {p["key"]: p for p in json.loads((ROOT / ".paper/reference_sources.json").read_text())["references"]}
    results = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = {executor.submit(audit, item, provenance[item["ID"]], args.out, args.refresh): item["ID"]
                   for item in entries}
        for future in as_completed(futures):
            result = future.result()
            results.append(result)
            n_match = sum(s.get("title_matches") is True for s in result["sources"])
            print(f"{result['key']}: {n_match}/{len(result['sources'])} source titles match", flush=True)
    report = {"checked_at": datetime.now(timezone.utc).isoformat(),
              "scope": "Identity screening only; NOT a claim-support or full publication-metadata certification.",
              "bibliography_sha256": hashlib.sha256((ROOT / "references.bib").read_bytes()).hexdigest(),
              "entries": sorted(results, key=lambda x: x["key"])}
    target = args.out / "identity-screen.json"
    target.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(f"Saved {len(results)} records to {target}")


if __name__ == "__main__":
    main()
