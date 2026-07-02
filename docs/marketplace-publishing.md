# Marketplace Publishing Notes

Research date: 2026-07-02.

This document tracks realistic publication and promotion paths for `Wangmerlyn/extract-chart-data-grounded`. It separates what can be prepared from this repository from steps that need the owner's marketplace login.

## Submission Kit

- Repository: <https://github.com/Wangmerlyn/extract-chart-data-grounded>
- Skill name: `extract-chart-data-grounded`
- Display name: Grounded Chart Data Extraction
- One-line pitch: Extract chart data from pixel-grounded visual markers, calibration metadata, overlays, and audit-ready tables.
- Repository license: `CC-BY-4.0` with attribution to Siyuan Wang / Wangmerlyn.
- Tags: `chart-extraction`, `data-digitization`, `scientific-figures`, `image-analysis`, `calibration`, `grounded-ai`
- Category candidates: data analysis, research, science, computer vision, productivity
- Primary prompt: `Use $extract-chart-data-grounded to extract data from this chart using pixel-grounded marker evidence. Save calibration metadata, raw pixel/marker tables, grounding overlays, reconstructed plots, and a final unit-converted table with limitations.`

## Platform Matrix

| Platform | Current fit | Publish path | Login needed | Notes |
| --- | --- | --- | --- | --- |
| ClawHub | Not a target. | Do not publish while `CC-BY-4.0` attribution is required. | Yes for real publish. | ClawHub docs say published skills are released under MIT-0 and per-skill license overrides are not supported, so this platform conflicts with the repo's attribution requirement. |
| Hermes Agent | Good for direct URL install. | `hermes skills install https://raw.githubusercontent.com/Wangmerlyn/extract-chart-data-grounded/main/SKILL.md --name extract-chart-data-grounded`. | No for public raw URL install. | Hermes also integrates skills.sh, LobeHub, well-known URLs, direct GitHub installs, and custom GitHub taps. A tap layout can be added later if this becomes a multi-skill catalog. |
| skills.sh / Vercel Labs skills CLI | Good. Verified via CLI list. | `npx skills add Wangmerlyn/extract-chart-data-grounded --list`. Users can install with `--skill extract-chart-data-grounded`. | No for public repo installs. | The CLI resolves GitHub repos, full URLs, direct skill paths, git URLs, and local paths. |
| SkillDock | Plausible. Current root is a clean skill folder. | `skilldock skill verify "$SKILL_PATH"` then `skilldock skill upload --namespace "$NAMESPACE" --slug extract-chart-data-grounded --version "$VERSION" --path "$SKILL_PATH" --dry-run`. | Yes for upload; Google OAuth or saved token. | Docs recommend verifying and dry-run uploading before release. |
| LobeHub skills catalog | Possible but not fully verified without an account/form. | Inspect the public submit flow, then use this README and `SKILL.md` as the listing source. | Likely yes. | Hermes lists LobeHub as an integrated community marketplace source. |
| Claude Code plugin marketplace repo | Possible, but this repo is not currently a plugin marketplace. | Requires a plugin manifest and marketplace repository shape. | No central submission path verified. | Only worth doing if you want Claude Code users to add this repo as a plugin marketplace. |
| GitHub `gh skill` tooling | Revisit after upgrading GitHub CLI. | Local `gh` 2.45.0 does not include `gh skill`. | GitHub auth likely needed for publish. | Current repo is still installable through generic GitHub-based skill tools. |

## Hermes Promotion

Use direct URL install first because the repo is a single root skill:

```bash
hermes skills install \
  https://raw.githubusercontent.com/Wangmerlyn/extract-chart-data-grounded/main/SKILL.md \
  --name extract-chart-data-grounded
```

If the repository later becomes a multi-skill catalog, add a `skills/extract-chart-data-grounded/` folder and use:

```bash
hermes skills tap add Wangmerlyn/extract-chart-data-grounded
```

Do not add the tap layout now unless the duplicate `SKILL.md` can be kept in sync automatically.

## SkillDock Workflow

SkillDock upload needs an account token:

```bash
python3 -m pip install --upgrade skilldock
skilldock auth login
skilldock tokens create --save
skilldock skill verify .
skilldock skill upload \
  --namespace "$NAMESPACE" \
  --slug extract-chart-data-grounded \
  --version "$VERSION" \
  --path . \
  --homepage-url https://github.com/Wangmerlyn/extract-chart-data-grounded \
  --dry-run
```

Remove `--dry-run` only after the owner confirms namespace and version.

## What Still Needs Owner Login

- ClawHub live publish: intentionally not pursued because ClawHub releases skills under MIT-0 rather than this repo's `CC-BY-4.0` attribution terms.
- SkillDock live upload: needs Google OAuth or saved SkillDock token and namespace ownership.
- LobeHub submission: likely needs a signed-in submitter; unauthenticated mechanics were not fully inspectable.
- GitHub `gh skill`: local GitHub CLI on this machine does not expose the command yet.

## Sources Checked

- ClawHub README and CLI docs: <https://github.com/openclaw/clawhub>
- ClawHub skill format: <https://github.com/openclaw/clawhub/blob/main/docs/skill-format.md>
- Hermes skills system: <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
- Vercel Labs skills CLI: <https://github.com/vercel-labs/skills>
- Agent Skills specification: <https://agentskills.io/specification>
- SkillDock publish docs: <https://docs.skilldock.io/publish>
- Anthropic skills repository: <https://github.com/anthropics/skills>
