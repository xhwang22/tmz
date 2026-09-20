# Landscape composite: balanced synthetic display

SIMULATED layout fixture, not experimental evidence or expected performance.
This is the author's approved v20 landscape composition, inserted in the paper
on 2026-09-19; now shown as appendix Figure 4. The full-cohort displays remain separate.

## Data and denominators

- Source: `../c1_groups.csv`, OOD only, 160 synthetic inputs per task.
- Rank SHA256(`20260918|domain|input_group`) without reading outcomes.
  Take 120 per task in the six-task families and 144 in the five-task families.
  This gives 720 per family, 2,880 total and 11,520 candidate slots.
- Keep the same selected inputs for all seven source methods, including
  incomplete responses; display five methods. Every input ID is synthetic.
- Agreement and Best-of-4 use each method's complete inputs. Assigned cost
  retains all selected inputs. Setting means equally weight eleven domains.
- Intervals are the 2.5/97.5 percentiles of 1,000 input-group bootstrap means.
  The per-task/method NumPy seed is the first 16 hex digits of the selection
  hash with `input_group=bootstrap-<method>`. These are marginal intervals,
  not paired tests or evidence of superiority.

## Published artifacts

`selected-inputs.csv` records the outcome-blind selection. `method-summaries.csv`,
`displayed-bars.csv` and `displayed-macros.csv` retain full precision.
Composition and task-catalog exports link codes to task names and input counts.
Point and bar geometry exports preserve the displayed coordinates; color exports
record categorical styling, not additional observations.

The exact PDF, SVG and PNG are in `figures/simulated/landscape_outcomes.*`.
They use Source Sans 3 and Source Serif 4, a 5.4 × 3.57-inch canvas, pale family
ramps for baselines and a common lake-green ERA accent. These are frozen vector
assets from the approved preview, not a new standalone rendering pipeline.
Historical exploratory renderers and their build-directory dependencies are not
required by a clean checkout. The old full-cohort atlas remains archived.
Trailing whitespace in the SVG was normalized for publication; its geometry,
data and styling are unchanged, as are the PDF and PNG exports.

Run `python3 scripts/check_landscape_results.py` from the repository root.
This independently replays selection, arithmetic, bootstrap intervals and
coordinates, and verifies hashes against the published assets. It does not
render a new plot or validate an empirical claim. Editing any source fixture
requires reviewing the resulting chart and updating its provenance, not merely
refreshing hashes. `make check` runs this audit too.

The 2026-09-19 appendix move changes the manifest's display ID to Fig4 and
replaces the checker's obsolete Figure 2 wording in its docstring and status
message. Only that checker hash is refreshed; the audit logic and every data,
geometry, and figure-asset hash remain unchanged.
