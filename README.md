# OpenModels Skills Registry

A community-maintained catalog of AI agent skills — structured, searchable, and integrated with the [OpenModels](https://openmodels.run) ecosystem.

## What are Skills?

Skills are structured definitions of tasks that AI agents excel at. Each skill includes:

- **Description** — what the skill does and when to use it
- **Recommended models** — which LLMs work best (linked to OpenModels registry)
- **Example prompts** — ready-to-use templates
- **Metadata** — category, complexity, modalities, compatible tools

Skills help developers discover what AI agents can do and choose the right model for each task.

## Quick Start

Browse skills on [openmodels.run/skills](https://openmodels.run/skills) or explore the YAML files directly:

```
skills/
├── code-review.yaml
├── unit-test-generation.yaml
├── refactoring-assistant.yaml
├── debugging-assistant.yaml
├── api-design.yaml
├── sql-generation.yaml
├── schema-design.yaml
├── documentation-generator.yaml
├── security-audit.yaml
├── accessibility-review.yaml
├── performance-optimization.yaml
├── ci-cd-pipeline.yaml
├── commit-message-writer.yaml
├── prompt-engineering.yaml
├── code-translation.yaml
└── regex-builder.yaml
```

## Skill Format

Each skill is a YAML file validated against a [JSON Schema](schemas/skill.schema.json):

```yaml
id: code-review
name: Code Review
description: >
  Automated code review with actionable feedback...
category: development
tags:
  - code-quality
  - automation
author:
  name: OpenModels Community
  github: openmodelsrun
recommended_models:
  - claude-opus-4-6
  - gpt-5
  - gemini-2-5-pro
min_context_window: 32000
modalities:
  input: [code, text]
  output: [text, code]
complexity: intermediate
use_cases:
  - Pull request review automation
  - Code quality gates in CI
example_prompt: |
  Review the following code for bugs, performance, and style...
related_skills:
  - unit-test-generation
  - security-audit
compatible_tools:
  - claude-code
  - cursor
  - kiro
  - any
created_at: "2026-05-24T10:00:00.000Z"
updated_at: "2026-05-24T10:00:00.000Z"
```

## Categories

| Category | Description |
|----------|-------------|
| 💻 development | Writing, reviewing, and improving code |
| ✍️ writing | Generating and transforming written content |
| 📊 data | Analyzing, transforming, and visualizing data |
| 🔍 research | Gathering and synthesizing information |
| 🎨 creative | Brainstorming and creative problem-solving |
| ⚙️ ops | Deployment, CI/CD, and infrastructure |
| 🧪 testing | Test generation and quality assurance |
| 🔒 security | Vulnerability detection and hardening |
| 🚀 productivity | Workflow automation and efficiency |

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Quick steps:**

1. Fork this repository
2. Create a new YAML file in `skills/` following the schema
3. Run validation: `python validate.py`
4. Submit a pull request

## Validation

All skills are validated against JSON Schema on every PR:

```bash
pip install -r requirements.txt
python validate.py
```

Validation checks:
- YAML syntax
- Schema conformance (required fields, types, enums, patterns)
- No duplicate IDs
- Filename matches the `id` field
- Related skills reference existing IDs

## Integration with OpenModels

Skills are ingested into the OpenModels platform and available via:

- **Web UI** — browse, filter, and search at [openmodels.run/skills](https://openmodels.run/skills)
- **API** — query programmatically via `/api/v1/skills`
- **Cross-references** — skills link to models, models link to skills

## License

MIT
