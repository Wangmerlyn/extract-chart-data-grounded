# Grounded Chart Data Extraction

[![skills.sh](https://skills.sh/b/Wangmerlyn/extract-chart-data-grounded)](https://skills.sh/Wangmerlyn/extract-chart-data-grounded)

This repository contains the `extract-chart-data-grounded` agent skill. It guides Codex and other Agent Skills-compatible systems to recover numeric data from chart images through measurable pixel evidence, calibration metadata, overlays, and audit-ready tables rather than visual estimates.

## What This Skill Does

The skill is for chart digitization work where the answer should be grounded in the image itself. It tells the agent to:

- preserve the source chart and record image metadata;
- locate axes, tick marks, plot boxes, legends, and plotted marks;
- fit the chart coordinate system before reading data values;
- save pixel-native evidence and unit-converted tables separately;
- validate the result with grounding overlays and reconstructed plots;
- state the precision limits of raster, scanned, compressed, or distorted images.

## When To Use It

Use this skill for raster chart images, scanned plots, screenshots, chromatograms, line charts, scatter plots, bar charts, multi-panel scientific figures, and unit-conversion requests where traceable data recovery matters.

Do not use it when vector source data, a source table, or the original analysis file is available. In that case, extract from the higher-fidelity source first and use the image only for verification.

## What It Produces

A complete extraction should leave an auditable output directory:

```text
output/
  source/
  calibration.json
  mark-pixels.csv
  final-unit-converted-table.csv
  grounding-overlay.png
  reconstructed-series.png
  extraction.log
  method-and-results.md
```

For quick feasibility checks or single-value reads, the skill still requires a source reference, calibration notes, annotated evidence or overlay, extracted value(s), and limitations.

## Quick Marketplace Review

- Skill file: `SKILL.md` at the repository root.
- Skill name: `extract-chart-data-grounded`.
- Runtime dependencies: none declared. The skill instructs agents to choose appropriate local image-processing tools for the chart at hand.
- Local discovery: `npx skills add . --list` discovers the root skill from the current checkout.
- Public discovery: `npx skills add Wangmerlyn/extract-chart-data-grounded --list` discovers the published GitHub repo.
- ClawHub is not a publication target because ClawHub-published skills are released under MIT-0, which conflicts with this repository's attribution requirement.

See [docs/marketplace-publishing.md](docs/marketplace-publishing.md) for current market-specific steps and login requirements.

## Install Or Try

Codex local skill install:

```bash
git clone https://github.com/Wangmerlyn/extract-chart-data-grounded \
  "${CODEX_HOME:-$HOME/.codex}/skills/extract-chart-data-grounded"
```

skills.sh compatible install:

```bash
npx skills add Wangmerlyn/extract-chart-data-grounded \
  --skill extract-chart-data-grounded \
  --agent codex \
  --global \
  --yes
```

Hermes direct URL install:

```bash
hermes skills install \
  https://raw.githubusercontent.com/Wangmerlyn/extract-chart-data-grounded/main/SKILL.md \
  --name extract-chart-data-grounded
```

## Example User Requests

- "Extract the plotted data from this scanned line chart and save calibration evidence."
- "Digitize this chromatogram peak trace and report pixel-grounded uncertainty."
- "Recover the bar values from this screenshot, including an overlay and calibration notes."
- "Convert the curve in this plot from pixels to the chart units and give me the raw pixel table too."
- "Check whether this image has enough resolution for reliable data extraction before building the full table."

## Limitations And Safety Notes

Raster charts are not mathematically lossless sources for original data. Compression, image resolution, line thickness, marker overlap, scan skew, and label occlusion can limit precision. The skill should produce an evidence chain, not claim exact recovery of hidden source data.

If overlays do not align, calibration residuals are large, or raw mark evidence is missing, the agent should recalibrate or disclose the limitation instead of publishing confident numeric claims.

## License

This repository is licensed under Creative Commons Attribution 4.0 International (`CC-BY-4.0`). You can copy, adapt, redistribute, and use the skill commercially as long as you credit Siyuan Wang / Wangmerlyn, link to the license, indicate whether you changed the material, and link back to this repository when practical.

Preferred attribution is in [NOTICE.md](NOTICE.md).

Important marketplace note: ClawHub currently publishes skills under MIT-0 and does not support per-skill license overrides. This repository should not be uploaded to ClawHub while attribution is required.

## Development

This repo intentionally keeps the runtime skill small. Human-facing packaging and marketplace notes belong in `README.md`, `AGENTS.md`, or `docs/`, while agent-facing extraction procedure belongs in `SKILL.md`.

Basic validation:

```bash
python - <<'PY'
import pathlib, yaml
text = pathlib.Path("SKILL.md").read_text()
assert text.startswith("---\n")
frontmatter = text.split("---\n", 2)[1]
data = yaml.safe_load(frontmatter)
assert data["name"] == "extract-chart-data-grounded"
assert data["description"]
yaml.safe_load(pathlib.Path("agents/openai.yaml").read_text())
print("skill metadata ok")
PY

git diff --check
npx skills add . --list
```
