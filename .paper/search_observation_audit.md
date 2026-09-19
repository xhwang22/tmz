# Development-search observation audit

Inspected: 2026-09-19.
Scope: qualitative motivation for the revised abstract and introduction (C43), not a confirmatory result.

## Evidence inspected

The author's private development report and original `step_record.json` files were inspected read-only.
The source was the default SkillOpt pointwise workflow in the September 17 development comparison.
Despite the historical collection name, these records concern the pointwise scoring arm.
The report's numerical results, sample identities, prompts, and private execution paths are not copied into this repository.

The report snapshot has SHA-256 `532a91b7944055e41be26ed72318e41c6372a9575b52941c82b05b7f33daddeb`.
The inspected record identities are:

| Step record | SHA-256 |
| --- | --- |
| `step_0001/step_record.json` | `d7bdd841aa7f47ce4790579704ecbdaea2dff21daba2fc73b17ee0a2b06ea3ce` |
| `step_0002/step_record.json` | `36dafdba31adcdcabbfc4fb18bb5c05234cf38a36447281596b45ad1e72c29ff` |
| `step_0003/step_record.json` | `0163b458b4eb09953df9ad14d4413e2c28efa2993fb05d23dbdb0ae3501bbdc9` |
| `step_0004/step_record.json` | `264b3b571e734a51236981906d13a5a0e40c6a78a5590a9ac083ef32b538bdad` |
| `step_0005/step_record.json` | `20af1a20df532e1603566d499fd6e5e8cb19ce1d2f146b2a33c29fb7d54200ba` |
| `step_0006/step_record.json` | `703ed0325839b671ddb4844165a2553db9a3a9cc75819dc44adcf91b9020baf0` |
| `step_0007/step_record.json` | `6f36e4aaef4dfe508439505868f910b86f22003ccc5fcf233dde53571d1fc6fe` |
| `step_0008/step_record.json` | `9b5af11e3a2f73c0e0219cb6e3773ce163f8139ffae20776c6e56bfa46a18257` |

## Supported observation

The `action`, `current_origin`, and `best_origin` fields show repeated rejection followed by retention of the incumbent, rather than continuation from the rejected implementation.
The accompanying proposal analysis describes shifts among task priorities, evidence interpretation, scope, and score calibration.
Related semantic themes can recur without preserving the rejected implementation as the next working candidate.
The manuscript therefore describes rejection and redirection, not disappearance of every idea from memory.
The records also contain accepted improvements; a blanket statement that nothing improved would be false.

## Interpretation and open test

The proposed explanation is that immediate candidate performance can end work on a direction before the implementation realizes the intended evaluation behavior.
That is a motivation for separating continuation from adoption, not an established causal account of all unsuccessful evolution.
The records do not show that arbitrary unsuccessful directions deserve more effort, that all RSI methods behave this way, or that depth-first search already wins.
Existing comparative development results do not establish an ERA advantage.
The continuation hypothesis remains C28, with `gap` status, pending matched-resource controls and independent evaluation.
The full publication-facing trajectory analysis remains to be prepared from authorized evidence; this internal audit is not a substitute for it.
