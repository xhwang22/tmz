"""Shared print-scale arrowheads for the two manuscript diagrams.

Arrowheads use explicit user-space dimensions, so a thicker route does not
silently enlarge its tip. The path has a shallow inset and softened corners;
it remains a compact, filled arrow at the manuscript's 5.4-inch print width.
"""
from html import escape

STYLE = "compact-filled-tips-rounded-routes"


def audit_markers(root):
    """Check the actual SVG, including tip/shaft color and reference wiring."""
    ns = {"s": "http://www.w3.org/2000/svg"}
    markers = {m.get("id"): m for m in root.findall(".//s:marker", ns)}
    assert markers, "No connector markers"
    for identifier, marker in markers.items():
        assert marker.get("markerUnits") == "userSpaceOnUse", identifier
        assert marker.get("viewBox") == "-1 -5.5 13 11", identifier
        assert marker.get("refX") == "11" and marker.get("refY") == "0", identifier
        assert marker.get("overflow") == "visible", identifier
        assert 6 <= float(marker.get("markerWidth")) <= 14, identifier
        tip = marker.find("s:path", ns)
        assert tip is not None and tip.get("fill") not in (None, "none"), identifier
        assert tip.get("stroke") == "none", identifier
    count = 0
    for path in root.findall(".//s:path", ns):
        reference = path.get("marker-end")
        if reference is None:
            continue
        assert reference.startswith("url(#") and reference.endswith(")"), reference
        identifier = reference[5:-1]
        assert identifier in markers, reference
        tip = markers[identifier].find("s:path", ns)
        assert tip.get("fill") == path.get("stroke"), (identifier, "head/shaft mismatch")
        assert path.get("stroke-linecap") == "round", identifier
        assert path.get("stroke-linejoin") == "round", identifier
        count += 1
    return count


def arrow_marker(identifier, color, length=12, height=9):
    return (
        f'<marker id="{escape(identifier)}" viewBox="-1 -5.5 13 11" '
        f'markerWidth="{length:g}" markerHeight="{height:g}" '
        'refX="11" refY="0" orient="auto" markerUnits="userSpaceOnUse" '
        'preserveAspectRatio="none" overflow="visible">'
        '<path d="M0 -4.4 L10.6 -0.55 Q11.7 0 10.6 0.55 L0 4.4 '
        'Q-0.8 4.8 -0.5 3.85 L0.9 0 L-0.5 -3.85 Q-0.8 -4.8 0 -4.4 Z" '
        f'fill="{escape(color)}" stroke="none"/></marker>'
    )


def underbrace(left, right, top, center, depth=11):
    """A shallow joining brace with tangent-continuous shoulders and a cusp.

    The center can follow the downstream connection rather than the midpoint
    of unequal input arms. Endpoints, shoulder baseline and cusp stay explicit.
    """
    assert left + 20 < center < right - 20
    shoulder = top + depth * .55
    tip = top + depth
    return (
        f'M{left:g} {top:g} C{left:g} {shoulder:g} {left+4:g} {shoulder:g} {left+11:g} {shoulder:g} '
        f'H{center-15:g} C{center-7:g} {shoulder:g} {center-5:g} {shoulder:g} {center:g} {tip:g} '
        f'C{center+5:g} {shoulder:g} {center+7:g} {shoulder:g} {center+15:g} {shoulder:g} '
        f'H{right-11:g} C{right-4:g} {shoulder:g} {right:g} {shoulder:g} {right:g} {top:g}'
    )
