# Repository Guidelines

## Purpose

This repository packages one Agent Skills-compatible skill: `extract-chart-data-grounded`. Keep `SKILL.md` focused on the procedure an agent needs at runtime. Put reviewer-facing context, install commands, and marketplace publication notes in `README.md` or `docs/`.

## Editing Rules

- Preserve the evidence-chain framing: source image, calibration, pixel or marker evidence, overlays, reconstructed plots, final table, and limitations.
- Do not add bulky generated extraction outputs, sample datasets, virtual environments, caches, or screenshots to the repository.
- Keep `SKILL.md` concise and procedural. Move long examples or market-specific details out of the runtime skill.
- After changing `SKILL.md`, verify `agents/openai.yaml` still describes the same trigger surface and includes `$extract-chart-data-grounded` in `interface.default_prompt`.
- Update `README.md` and `docs/marketplace-publishing.md` when marketplace commands, login requirements, or verified compatibility changes.
- Preserve the repository license and attribution notice unless the owner explicitly changes the licensing strategy.

## Validation

Run these checks before opening or merging a PR:

```bash
python - <<'PY'
import pathlib, yaml
text = pathlib.Path("SKILL.md").read_text()
assert text.startswith("---\n")
frontmatter = text.split("---\n", 2)[1]
data = yaml.safe_load(frontmatter)
assert data["name"] == "extract-chart-data-grounded"
assert data["description"]
openai = yaml.safe_load(pathlib.Path("agents/openai.yaml").read_text())
assert "$extract-chart-data-grounded" in openai["interface"]["default_prompt"]
print("skill metadata ok")
PY

git diff --check
npx skills add . --list
```

## Release And Marketplace Notes

- Do not publish this repository to ClawHub while the owner requires `CC-BY-4.0` attribution. ClawHub publishes skills under MIT-0 and cannot enforce the repository attribution requirement.
- SkillDock real upload requires SkillDock OAuth or a saved token.
- Hermes can consume the raw `SKILL.md` URL directly; a GitHub tap layout can be added later if this repo becomes a multi-skill catalog.
- Do not claim a marketplace submission is complete unless the platform returned a successful publish/install confirmation.
