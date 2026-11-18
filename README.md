# Grounded Chart Data Extraction

Recover numeric data from chart images using pixel measurements you can inspect.

`extract-chart-data-grounded` is an agent skill for Codex and other tools that support Agent Skills. Use it to digitize line charts, scatter plots, bar charts, chromatograms, and scanned scientific figures.

## Install

For Codex:

```bash
npx skills add Wangmerlyn/extract-chart-data-grounded \
  --skill extract-chart-data-grounded \
  --agent codex --global --yes
```

For manual installation, copy the [skill folder](skills/extract-chart-data-grounded) into your agent's skills directory. See the [marketplace guide](docs/marketplace-publishing.md) for Hermes commands and other distribution options.

## Use

Provide a chart image and ask:

```text
Use $extract-chart-data-grounded to extract the data from this chart.
Save the pixel measurements, axis calibration, an overlay showing the
measured points, and a final table in the chart's units. Explain the
precision limits.
```

The skill guides the agent to preserve the source image, calibrate the axes, measure the plotted marks, and check the results against the image.

## Outputs

A full extraction includes:

- The source image and calibration metadata.
- Raw pixel measurements and a table converted to the chart's units.
- An annotated overlay and a reconstructed plot for visual checking.
- A method summary, extraction log, and precision limits.

Quick checks and single-value reads still need a source reference, calibration notes, annotated evidence, and stated limitations.

## Accuracy

Use original tables or vector data when available. Image-based extraction is limited by resolution, compression, line thickness, overlapping marks, and scan distortion; it cannot guarantee exact recovery of the original data.

If calibration or overlays do not align, the agent should recalibrate or clearly explain the uncertainty.

## Development

The extraction procedure lives in [SKILL.md](skills/extract-chart-data-grounded/SKILL.md). To check the package:

```bash
python scripts/validate_package.py
git diff --check
```

See [AGENTS.md](AGENTS.md) for the full validation steps and [marketplace publishing notes](docs/marketplace-publishing.md) for distribution guidance.

## License

[CC BY 4.0](LICENSE), by Siyuan Wang / Wangmerlyn. See [NOTICE.md](NOTICE.md) for attribution.
