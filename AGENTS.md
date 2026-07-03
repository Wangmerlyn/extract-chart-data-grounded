# Repository Guidelines

## Purpose

This repository packages one Agent Skills-compatible skill: `extract-chart-data-grounded`. The canonical runtime file is `skills/extract-chart-data-grounded/SKILL.md`. Keep that file focused on the procedure an agent needs at runtime. Put reviewer-facing context, install commands, and marketplace publication notes in `README.md` or `docs/`.

## Editing Rules

- Preserve the evidence-chain framing: source image, calibration, pixel or marker evidence, overlays, reconstructed plots, final table, and limitations.
- Do not add bulky generated extraction outputs, sample datasets, virtual environments, caches, or screenshots to the repository.
- Keep `skills/extract-chart-data-grounded/SKILL.md` concise and procedural. Move long examples or market-specific details out of the runtime skill.
- Do not add a duplicate root `SKILL.md`; the nested `skills/` layout is canonical for Hermes taps and compatible with SkillsMP-style indexing.
- After changing `skills/extract-chart-data-grounded/SKILL.md`, verify `agents/openai.yaml` still describes the same trigger surface and includes `$extract-chart-data-grounded` in `interface.default_prompt`.
- Update `README.md` and `docs/marketplace-publishing.md` when marketplace commands, login requirements, or verified compatibility changes.
- Preserve the repository license and attribution notice unless the owner explicitly changes the licensing strategy.

## Validation

Run these checks before opening or merging a PR:

```bash
python scripts/validate_package.py
git diff --check
tmpdir="$(mktemp -d)"
trap 'rm -rf "$tmpdir"' EXIT
cp -a . "$tmpdir/repo"
npx --yes skills add "$tmpdir/repo" --list
```

## Release And Marketplace Notes

- Do not publish this repository to ClawHub while the owner requires `CC-BY-4.0` attribution. ClawHub publishes skills under MIT-0 and cannot enforce the repository attribution requirement.
- SkillDock real upload requires SkillDock OAuth or a saved token.
- Hermes can consume the raw nested `SKILL.md` URL directly, and `hermes skills tap add Wangmerlyn/extract-chart-data-grounded` can scan the default `skills/` layout.
- SkillsMP aggregates public GitHub Agent Skills and does not appear to force relicensing, but do not claim this repo is indexed there until its public API or skill page returns this repository.
- Do not claim a marketplace submission is complete unless the platform returned a successful publish/install confirmation.
