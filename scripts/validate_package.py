from __future__ import annotations

import json
import pathlib

import yaml


ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "extract-chart-data-grounded" / "SKILL.md"
OPENAI_CONFIG = ROOT / "agents" / "openai.yaml"
SKILLS_SH = ROOT / "skills.sh.json"


def main() -> None:
    assert not (ROOT / "SKILL.md").exists(), "root SKILL.md would duplicate the canonical nested skill"
    text = SKILL.read_text()
    assert text.startswith("---\n"), "SKILL.md must start with YAML frontmatter"
    data = yaml.safe_load(text.split("---\n", 2)[1])

    assert data["name"] == "extract-chart-data-grounded"
    assert data["description"]
    assert data["license"] == "CC-BY-4.0"

    metadata = data["metadata"]
    assert metadata["author"] == "Siyuan Wang / Wangmerlyn"
    assert metadata["source"] == "https://github.com/Wangmerlyn/extract-chart-data-grounded"
    assert metadata["license_url"] == "https://creativecommons.org/licenses/by/4.0/"
    assert metadata["version"] == "1.0.0"
    assert "chart-extraction" in metadata["tags"]
    assert all(isinstance(value, str) for value in metadata.values())

    openai = yaml.safe_load(OPENAI_CONFIG.read_text())
    assert "$extract-chart-data-grounded" in openai["interface"]["default_prompt"]

    catalog = json.loads(SKILLS_SH.read_text())
    grouped_skills = {
        skill
        for grouping in catalog["groupings"]
        for skill in grouping["skills"]
    }
    assert catalog["$schema"] == "https://skills.sh/schemas/skills.sh.schema.json"
    assert "extract-chart-data-grounded" in grouped_skills

    print("skill package metadata ok")


if __name__ == "__main__":
    main()
