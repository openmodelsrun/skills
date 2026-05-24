# Changelog

All notable changes to the OpenModels Skills Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-05-24

### Added

- Initial release of the OpenModels Skills Registry
- JSON Schema for skill validation (`schemas/skill.schema.json`)
- JSON Schema for category validation (`schemas/category.schema.json`)
- 9 skill categories: development, writing, data, research, creative, ops, testing, security, productivity
- 15 seed skills:
  - `accessibility-review` — WCAG 2.1 AA compliance review
  - `api-design` — RESTful and GraphQL API design
  - `ci-cd-pipeline` — CI/CD pipeline builder
  - `code-review` — Automated code review
  - `code-translation` — Cross-language code translation
  - `commit-message-writer` — Conventional commit messages
  - `data-analysis` — Exploratory data analysis
  - `debugging-assistant` — Systematic debugging workflow
  - `documentation-generator` — Documentation from code
  - `performance-optimization` — Performance bottleneck analysis
  - `prompt-engineering` — LLM prompt design and optimization
  - `refactoring-assistant` — Systematic code refactoring
  - `regex-builder` — Regex from natural language
  - `schema-design` — Database schema design
  - `security-audit` — Security vulnerability detection
  - `sql-generation` — SQL from natural language
  - `unit-test-generation` — Comprehensive unit test generation
- Python validation script (`validate.py`)
