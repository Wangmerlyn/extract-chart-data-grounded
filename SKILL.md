---
name: extract-chart-data-grounded
description: Use when Codex needs to extract, digitize, recover, or unit-convert numeric data from raster chart images, scanned plots, chromatograms, line charts, scatter plots, bar charts, or screenshots where visual marker grounding, axis calibration, tick detection, overlays, pixel evidence, or chart-to-table precision matters.
---

# Extract Chart Data Grounded

## Overview

Extract chart data from visual evidence, not from visual guessing. Treat the image as measurable data: identify plotted marks and calibration markers, preserve pixel evidence, fit the chart coordinate system, and only then output unit-converted tables.

Raster charts are not mathematically lossless sources for the original data. The lossless artifact is the evidence chain: source image, selected pixels/markers, calibration metadata, overlays, logs, and reproducible outputs.

## Core Rules

- Do not estimate table values by eye when pixel extraction or marker measurement is possible.
- Do not claim exact original source data from a raster image. State the precision limit imposed by image resolution, compression, scan distortion, line thickness, and overlapping text.
- Create a task-specific output directory and save all process outputs there.
- Keep raw evidence separate from derived interpretations. Interpolated, smoothed, or resampled tables must be labeled as derived.
- Before finalizing, inspect grounding overlays. If axes, ticks, plot box, or selected marks do not align, recalibrate.
- For scanned or tilted charts, test whether orthogonal axes are wrong. Prefer affine, skew-aware, or projective calibration when marker geometry shows tilt.

## Workflow

1. Preserve the source
   - Copy or reference the original image.
   - Record image size, file hash, source path, and any user-provided chart units.
   - If vector/source data is available, extract from that source first and use the raster only for verification.

2. Locate grounding markers
   - Detect axis spines, tick marks, gridlines, plot box corners, labels, legends, and series colors/markers.
   - Use actual marker coordinates, not approximate visual impressions.
   - For each axis, record matched tick/marker positions, expected data values, residuals, and rejected outliers.

3. Calibrate the coordinate system
   - Fit the simplest coordinate model that matches the image: orthogonal, affine/skewed, log-scale, categorical, polar, multi-panel, or secondary axis as needed.
   - For scanned charts, fit axis lines from tick endpoints or plot-box edges and transform points through that fitted frame.
   - Report calibration residuals in pixels. If residuals are large or patterned, revisit marker detection instead of forcing the table.

4. Extract plotted marks
   - Segment marks using image-grounded evidence such as color, grayscale threshold, connected components, edge/line structure, or marker shape.
   - Save every selected pixel or detected marker center with pixel coordinates and calibrated data coordinates.
   - Preserve alternate interpretations when line thickness matters, such as top envelope, centerline, median, bottom edge, peak apex, or bar edge.
   - Remove text, axes, labels, and noise only with documented rules and saved masks/overlays.

5. Convert units and build tables
   - Produce a primary unit-converted table in chart units.
   - Keep a pixel-native table for audit.
   - If interpolation is useful, create a separate interpolated table and label it as derived.
   - Do not fabricate values outside the reliable extracted range; report the reliable range explicitly.

6. Validate visually and numerically
   - Generate overlays showing source image, fitted axes/ticks, selected pixels/marks, plot box, and reconstructed values.
   - Reconstruct the extracted series as an image or plot and compare it with the source.
   - Verify row counts, calibration metadata, and peak/key-point values from files rather than memory.
   - Open the grounding overlay before finalizing. Confirm tick residuals are reported in pixels, selected marks align with visible marks, and every final table row traces back to a saved pixel or marker record.
   - If the required artifacts cannot be generated, withhold numeric certainty and explain which evidence is missing.

## Minimum Deliverables

Save enough artifacts for another agent or user to audit the extraction:

- `source/`: original chart image or exact source reference.
- `calibration.json`: image size, axis/tick markers, transform parameters, residuals, units, thresholds, filtering rules, and row counts.
- `curve-pixels.csv` or `mark-pixels.csv`: raw selected pixel evidence with pixel coordinates and calibrated coordinates.
- `final-unit-converted-table.csv`: recommended table in chart units.
- Optional derived tables, such as interpolated or smoothed tables, clearly marked as derived.
- `grounding-overlay.png`: source image with detected axes, ticks, plot box, and selected data marks.
- `reconstructed-*.png`: plot or image reconstructed from extracted values.
- `extraction.log` or command notes sufficient to reproduce the run.
- `method-and-results.md`: concise explanation of calibration, extraction decisions, limitations, and where final tables live.

For partial or triage tasks, scale the artifact set down but keep the evidence chain intact: preserve the source reference, calibration notes, annotated evidence or overlay, extracted value(s), and limitations. Produce the full CSV/log bundle when the user asks for a complete extraction.

## Quality Bar

Before answering the user, confirm:

- The overlay aligns with the visual markers that define the chart coordinate system.
- The final table can be traced back to saved pixel or marker evidence.
- Unit conversion formulas are explicit.
- Any skew, rotation, log scale, categorical axis, multiple axis, or panel split is handled or documented as a limitation.
- Ambiguous regions, text overlaps, saturated peaks, missing data, and manual corrections are disclosed.

## Common Mistakes

| Mistake | Correction |
|---|---|
| Reading values directly from the image by sight | Extract pixels/markers and calibrate them. |
| Treating a scanned chart as perfectly horizontal/vertical | Fit axes from visual markers and use skew-aware calibration when needed. |
| Publishing only the final CSV | Save raw pixels, calibration JSON, overlays, and logs. |
| Mixing raw and interpolated rows | Put interpolated values in a separate derived table. |
| Claiming "lossless" original numeric data from raster | Say the pixel evidence is lossless; calibrated values are resolution-limited. |
