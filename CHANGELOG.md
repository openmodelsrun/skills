# Changelog

All notable changes to the OpenModels Skills Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.4] - 2026-05-26

### Added

- 10 new scientific and data skills inspired by K-Dense-AI/scientific-agent-skills and community needs:
  - `literature-review` — systematic literature reviews across PubMed, arXiv, bioRxiv, Semantic Scholar
  - `hypothesis-generation` — scientific hypothesis formulation, PICO frameworks, experimental design
  - `bioinformatics-pipeline` — scRNA-seq analysis, Scanpy, pathway enrichment, variant calling
  - `molecular-analysis` — cheminformatics with RDKit, drug-likeness, ADMET, SAR analysis
  - `scientific-visualization` — publication-quality figures, volcano plots, heatmaps, multi-panel layouts
  - `network-graph-analysis` — NetworkX, community detection, centrality, GNN, knowledge graphs
  - `time-series-forecasting` — ARIMA, Prophet, LSTM, anomaly detection, backtesting
  - `ml-experiment-tracker` — MLflow, Weights & Biases, Optuna, hyperparameter optimization
  - `scientific-writing` — manuscripts, grants, IMRaD structure, peer review responses
  - `geospatial-analysis` — GeoPandas, GIS, remote sensing, spatial statistics, choropleth maps

### Changed

- Total skills: 62 (from 51)

## [0.1.3] - 2026-05-25

### Added

- 10 new skills inspired by ModelScope Skills Marketplace and community trends:
  - `skill-vetter` — security-first auditing of agent skills before installation
  - `knowledge-graph` — typed knowledge graphs for structured agent memory
  - `cloud-deploy` — cloud deployment with Terraform, Docker, CI/CD generation
  - `github-workflow` — GitHub automation via gh CLI (PRs, issues, CI, releases)
  - `self-improving-agent` — continuous improvement via error recording and learning
  - `frontend-design` — production-grade UI with unique design quality
  - `ab-test-setup` — A/B experiment design with statistical rigor
  - `pptx-generator` — PowerPoint presentation generation from text
  - `web-summarizer` — web page and document summarization
  - `weather-lookup` — weather conditions and forecasts via free APIs

### Changed

- Total skills: 51

## [0.1.2] - 2026-05-25

### Added

- 6 new skills:
  - `system-design` — scalable distributed systems architecture
  - `ai-agent-builder` — AI agent design with tool definitions, MCP, orchestration
  - `api-client-generator` — type-safe SDK generation from OpenAPI specs
  - `landing-page-generator` — conversion-optimized landing pages from product briefs
  - `technical-writing` — ADRs, READMEs, runbooks, onboarding guides
  - `database-query-optimizer` — SQL optimization, indexing strategies, EXPLAIN analysis

### Changed

- Total skills: 41

## [0.1.1] - 2026-05-24

### Added

- 15 new skills:
  - `api-error-handler` — API error handling with RFC 7807
  - `brainstorm-facilitator` — structured ideation with SCAMPER, Six Hats
  - `changelog-generator` — changelogs from git history
  - `code-explainer` — explain code at any depth level
  - `cron-expression-builder` — cron from natural language
  - `dependency-auditor` — audit deps for vulnerabilities and licenses
  - `docker-compose-generator` — Docker Compose from requirements
  - `email-writer` — professional email drafting
  - `env-config-generator` — .env files and validation schemas
  - `error-message-improver` — rewrite errors for end users
  - `git-conflict-resolver` — resolve merge conflicts with intent analysis
  - `git-pr-description` — PR descriptions from diffs
  - `migration-planner` — framework/version migration strategies
  - `openapi-spec-generator` — OpenAPI 3.1 specs from code or descriptions
  - `react-component-generator` — production-ready React components
  - `research-summarizer` — summarize papers and articles
  - `test-data-generator` — realistic fixtures and seed data
  - `typescript-type-generator` — TypeScript types from JSON/schemas

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
