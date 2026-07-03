# Marketplace Publishing Notes

Research date: 2026-07-03.

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
| Hermes Agent | Good for direct URL and GitHub tap install. | `hermes skills install https://raw.githubusercontent.com/Wangmerlyn/extract-chart-data-grounded/main/skills/extract-chart-data-grounded/SKILL.md --name extract-chart-data-grounded`, or `hermes skills tap add Wangmerlyn/extract-chart-data-grounded` then `hermes skills install Wangmerlyn/extract-chart-data-grounded/extract-chart-data-grounded`. | No for public raw URL or tap install. GitHub publish uses `GITHUB_TOKEN`/`GH_TOKEN` or `gh auth token`. | Hermes taps scan `skills/` by default, with each skill under `skills/<skill-name>/SKILL.md`. Hermes publish to another catalog repo also uploads under `skills/<skill-name>/` after a Skills Guard scan. |
| SkillsMP | Good format fit; not yet confirmed as indexed. | Public GitHub repository with `skills/extract-chart-data-grounded/SKILL.md` frontmatter and root README/license context. | No for public search/API. Login or API key only raises API limits and enables account features. | SkillsMP indexes public GitHub `SKILL.md` sources and says public repos may be discovered in future indexing runs. Its public API search did not return this exact skill on 2026-07-03, so treat indexing as pending rather than complete. No forced marketplace relicensing was found. |
| skills.sh / Vercel Labs skills CLI | Good. Verified via CLI list. | `npx skills add Wangmerlyn/extract-chart-data-grounded --list`. Users can install with `--skill extract-chart-data-grounded`. | No for public repo installs. | The CLI resolves GitHub repos, full URLs, direct skill paths, git URLs, and local paths. |
| SkillDock | Plausible. Use the nested skill directory as the package path. | `skilldock skill verify skills/extract-chart-data-grounded` then `skilldock skill upload --namespace "$NAMESPACE" --slug extract-chart-data-grounded --version "$VERSION" --path skills/extract-chart-data-grounded --dry-run`. | Yes for upload; Google OAuth or saved token. | Docs recommend verifying and dry-run uploading before release. |
| LobeHub skills catalog | Possible but not fully verified without an account/form. | Inspect the public submit flow, then use this README and `skills/extract-chart-data-grounded/SKILL.md` as the listing source. | Likely yes. | Hermes lists LobeHub as an integrated community marketplace source. |
| Claude Code plugin marketplace repo | Possible, but this repo is not currently a plugin marketplace. | Requires a plugin manifest and marketplace repository shape. | No central submission path verified. | Only worth doing if you want Claude Code users to add this repo as a plugin marketplace. |
| GitHub `gh skill` tooling | Revisit after upgrading GitHub CLI. | Local `gh` 2.45.0 does not include `gh skill`. | GitHub auth likely needed for publish. | Current repo is still installable through generic GitHub-based skill tools. |

## Hermes Promotion

Use direct URL install first when sharing one command after the nested layout reaches `main`. It does not need a marketplace account:

```bash
hermes skills install \
  https://raw.githubusercontent.com/Wangmerlyn/extract-chart-data-grounded/main/skills/extract-chart-data-grounded/SKILL.md \
  --name extract-chart-data-grounded
```

The repository also has the default Hermes tap layout:

```bash
hermes skills tap add Wangmerlyn/extract-chart-data-grounded
hermes skills install Wangmerlyn/extract-chart-data-grounded/extract-chart-data-grounded
```

Hermes also has a GitHub publish flow for submitting the skill into a separate catalog repository:

```bash
hermes skills publish \
  /root/new_test/extract-chart-data-grounded/skills/extract-chart-data-grounded \
  --to github \
  --repo owner/skills-catalog
```

This command scans the skill, forks the target repository, uploads the skill under `skills/extract-chart-data-grounded/`, and opens a PR. Use it only after choosing the target catalog repository; do not point it at ClawHub.

## SkillsMP Notes

SkillsMP appears compatible with the same `SKILL.md` shape used here:

- It describes itself as an independent community directory that indexes public GitHub `SKILL.md` sources.
- Its agent-facing docs say skills follow the open `SKILL.md` standard with required `name` and `description` frontmatter, optional `license`, optional string key-value `metadata`, plus optional `scripts/`, `references/`, and `assets/` directories.
- Its public API returns skill records with `name`, `author`, `description`, `githubUrl`, `skillUrl`, stars, and update time.
- No SkillsMP-specific relicensing requirement was found. The site/API code license is not the same as a license grant for indexed skills.
- API search for `extract-chart-data-grounded` on 2026-07-03 returned related chart-extraction skills but not this exact repository, so do not claim SkillsMP publication until a SkillsMP result points to this repo.

Keep `python scripts/validate_package.py` in the release checklist so the canonical nested skill keeps the attribution metadata that raw URL installers see and no duplicate root `SKILL.md` is added.

## SkillDock Workflow

SkillDock upload needs an account token:

```bash
python3 -m pip install --upgrade skilldock
skilldock auth login
skilldock tokens create --save
skilldock skill verify skills/extract-chart-data-grounded
skilldock skill upload \
  --namespace "$NAMESPACE" \
  --slug extract-chart-data-grounded \
  --version "$VERSION" \
  --path skills/extract-chart-data-grounded \
  --homepage-url https://github.com/Wangmerlyn/extract-chart-data-grounded \
  --dry-run
```

Remove `--dry-run` only after the owner confirms namespace and version.

## What Still Needs Owner Login

- ClawHub live publish: intentionally not pursued because ClawHub releases skills under MIT-0 rather than this repo's `CC-BY-4.0` attribution terms.
- Hermes GitHub publish: needs a chosen target catalog repo. It can use this machine's authenticated `gh` token, but it will create a fork and PR to that target.
- SkillsMP indexing: no login is needed for public discovery, but manual promotion or account features may need sign-in. Do not claim indexing until the public SkillsMP API or page returns this repository.
- SkillDock live upload: needs Google OAuth or saved SkillDock token and namespace ownership.
- LobeHub submission: likely needs a signed-in submitter; unauthenticated mechanics were not fully inspectable.
- GitHub `gh skill`: local GitHub CLI on this machine does not expose the command yet.

## Sources Checked

- ClawHub README and CLI docs: <https://github.com/openclaw/clawhub>
- ClawHub skill format: <https://github.com/openclaw/clawhub/blob/main/docs/skill-format.md>
- Hermes skills system: <https://hermes-agent.nousresearch.com/docs/user-guide/features/skills>
- SkillsMP docs and API: <https://skillsmp.com/docs>, <https://skillsmp.com/docs/api>, <https://skillsmp.com/llms-full.txt>, <https://skillsmp.com/openapi.json>
- Vercel Labs skills CLI: <https://github.com/vercel-labs/skills>
- Agent Skills specification: <https://agentskills.io/specification>
- SkillDock publish docs: <https://docs.skilldock.io/publish>
- Anthropic skills repository: <https://github.com/anthropics/skills>
