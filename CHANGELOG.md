# Changelog

All notable changes to the OpenModels Skills Registry will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.9.0] - 2026-07-21
### Added
- 2 new skills tied to the latest Gemini Flash releases:
  - `computer-use-automation` for driving desktop/browser computer-use agents, matching the built-in computer use tool in Gemini 3.6 Flash and 3.5 Flash-Lite.
  - `vulnerability-remediation` for finding, validating, and auto-patching security issues, modeling a CodeMender-style workflow (Gemini 3.5 Flash Cyber).
### Changed
- Total skills: 205 (from 203).

## [0.8.0] - 2026-07-15

### Added

- 15 new skills for dependable AI, product, data, and engineering operations:
  - `agent-evals`, `red-team-simulation`, and `ai-agent-incident-response` for agent quality, safety, and operational recovery.
  - `llm-observability-design`, `data-contract-design`, `database-migration-planning`, and `analytics-instrumentation` for production reliability and data governance.
  - `accessibility-audit`, `release-notes-automation`, `customer-feedback-synthesis`, and `product-requirements-discovery` for product quality and discovery.
  - `api-versioning-strategy`, `secrets-rotation-design`, `infrastructure-cost-review`, and `incident-postmortem` for safe platform evolution and operations.

### Changed

- Total skills: 203 (from 188).

## [0.7.0] - 2026-07-15

### Added

- 15 new skills for production AI-agent, LLM quality, and developer workflows:
  - `agent-memory-design` — durable agent memory architecture with retrieval, retention, and privacy controls (development)
  - `ai-codebase-onboarding` — repository discovery and concise developer onboarding guides (development)
  - `architecture-decision-record` — reviewable ADRs with alternatives, trade-offs, and reversal criteria (development)
  - `browser-test-debugging` — diagnosis of E2E failures using traces, screenshots, network activity, and state (testing)
  - `design-to-code-implementation` — accessible responsive implementation from designs and screenshots (development)
  - `llm-output-evaluation` — representative datasets, rubrics, automated checks, and quality thresholds (testing)
  - `mcp-server-builder` — secure MCP server design, tool schemas, transports, and tests (development)
  - `mcp-server-security-review` — MCP permission, injection, secret-handling, and authorization review (security)
  - `model-context-budgeting` — context allocation and token-cost optimization for agents and RAG (ops)
  - `prompt-regression-testing` — regression suites and CI gates for prompts and agent instructions (testing)
  - `retrieval-evaluation` — retrieval metrics, failure taxonomy, and RAG tuning experiments (data)
  - `structured-output-design` — validated, versioned JSON contracts for LLM integrations (development)
  - `tool-call-testing` — integration tests for agent tools, authorization, side effects, and recovery (testing)
  - `ai-safety-policy-review` — actionable AI safety policies, escalation paths, and acceptance criteria (security)
  - `workflow-automation-design` — reliable AI-assisted automations with approvals, retries, and handoffs (productivity)

### Changed

- Total skills: 188 (from 173)

## [0.6.0] - 2026-07-12

### Added

- 15 new skills across 9 categories:
  - `caching-strategy-designer` — multi-layer caching plans with patterns, TTLs, and invalidation (development)
  - `rate-limiter-designer` — API rate limiting algorithms and distributed Redis enforcement (development)
  - `newsletter-writer` — email newsletters with subject lines and a single clear CTA (writing)
  - `case-study-writer` — challenge/solution/results customer case studies with verifiable metrics (writing)
  - `sql-query-explainer` — plain-language SQL explanations and EXPLAIN ANALYZE reading (data)
  - `dbt-model-generator` — layered dbt models with schema.yml tests and materialization strategy (data)
  - `survey-designer` — unbiased questionnaires with scales, branching, and an analysis plan (research)
  - `user-interview-guide-builder` — discovery/usability interview guides with non-leading probes (research)
  - `game-design-document-writer` — structured GDDs covering core loop, economy, and MVP scope (creative)
  - `ad-copy-writer` — conversion-focused search/social ad variants for A/B testing (creative)
  - `runbook-generator` — operational runbooks with diagnosis, remediation, rollback, and escalation (ops)
  - `disaster-recovery-planner` — DR/BC plans with RTO/RPO targets, failover, and game days (ops)
  - `test-plan-writer` — structured test plans with case derivation and traceability matrix (testing)
  - `penetration-test-planner` — scoped, authorized pentest plans aligned to OWASP/PTES (security)
  - `email-triage-assistant` — inbox triage with categorization, action extraction, and reply drafts (productivity)

### Changed

- Total skills: 173 (from 158)

## [0.5.0] - 2026-07-12

### Added

- 18 new skills across 8 categories:
  - `git-hooks-manager` — set up and maintain Git hooks (Husky/Lefthook/pre-commit) for linting, formatting, and secret scanning (development)
  - `blog-post-writer` — draft SEO-aware long-form blog posts from an outline or notes (writing)
  - `social-media-post-writer` — platform-tailored posts and threads for X, LinkedIn, and Instagram (writing)
  - `resume-optimizer` — rewrite resumes into ATS-friendly, achievement-focused documents (writing)
  - `csv-data-cleaner` — diagnose and fix messy tabular data with reproducible pandas/Polars code (data)
  - `data-storytelling` — turn analysis results into an audience-ready narrative with chart guidance (data)
  - `competitive-intelligence-analyst` — structured competitor matrices and SWOT from public info (research)
  - `fact-checker` — extract and rate factual claims for accuracy and verifiability (research)
  - `naming-generator` — product, feature, and company name candidates with rationale (creative)
  - `color-palette-generator` — accessible brand/UI palettes with WCAG contrast checks and tokens (creative)
  - `nginx-config-generator` — production-ready reverse proxy, TLS, and rate-limit configs (ops)
  - `ansible-playbook-writer` — idempotent Ansible playbooks and roles from a target state (ops)
  - `bdd-scenario-writer` — Gherkin acceptance scenarios and Cucumber/Behave step definitions (testing)
  - `visual-regression-tester` — screenshot-based visual regression suites with CI baselines (testing)
  - `jwt-analyzer` — decode and security-review JWTs and token validation flows (security)
  - `privacy-compliance-auditor` — GDPR/CCPA data-flow review and remediation backlog (security)
  - `task-prioritizer` — rank tasks with RICE, Eisenhower, or value/effort frameworks (productivity)
  - `decision-matrix-builder` — weighted decision matrices with sensitivity analysis for ADRs (productivity)

### Changed

- Total skills: 158 (from 140)

## [0.4.0] - 2026-07-09

### Added

- 20 new skills across 7 categories:
  - `oauth-flow-implementer` — secure OAuth 2.0/OIDC flows with PKCE and token handling (development)
  - `websocket-service-builder` — real-time WebSocket/SSE services with scaling and reconnection (development)
  - `cli-tool-builder` — ergonomic command-line tools with subcommands and completions (development)
  - `state-machine-designer` — statecharts/XState workflows that prevent impossible states (development)
  - `browser-extension-builder` — cross-browser Manifest V3 extensions (development)
  - `llm-cost-optimizer` — reduce LLM inference cost via caching, routing, and prompt trimming (development)
  - `model-router-designer` — route requests across LLMs by cost, latency, and difficulty (development)
  - `fine-tuning-dataset-curator` — curate SFT/DPO datasets with dedup, filtering, and contamination checks (data)
  - `recommendation-system-designer` — candidate generation, ranking, and cold-start strategy (data)
  - `data-contract-designer` — producer/consumer data contracts with compatibility and SLAs (data)
  - `terraform-module-writer` — reusable, validated Terraform modules with examples (ops)
  - `cloud-cost-optimizer` — FinOps plan for rightsizing, commitments, and cleanup (ops)
  - `chaos-experiment-designer` — safe chaos experiments with blast-radius limits (ops)
  - `e2e-test-scenario-writer` — resilient Playwright/Cypress end-to-end tests (testing)
  - `property-based-test-generator` — invariant/property tests with generators and shrinking (testing)
  - `mutation-testing-advisor` — measure and improve real test-suite effectiveness (testing)
  - `sbom-generator` — CycloneDX/SPDX software bills of materials with VEX (security)
  - `security-headers-configurator` — CSP, HSTS, and hardening headers with safe rollout (security)
  - `brand-voice-designer` — distinctive, consistent brand voice and tone guides (creative)
  - `okr-planner` — outcome-based Objectives and Key Results with cadence (productivity)

### Changed

- Total skills: 140 (from 120)

## [0.3.0] - 2026-07-09

### Added

- 17 new skills across 8 categories:
  - `observability-instrumentation` — add OpenTelemetry logs, metrics, and traces to a codebase (ops)
  - `slo-error-budget-planner` — define SLIs/SLOs and multi-burn-rate error budget alerts (ops)
  - `flaky-test-detector` — diagnose and fix nondeterministic tests (testing)
  - `contract-test-generator` — consumer-driven contract tests between services (testing)
  - `llm-eval-harness-builder` — evaluation harnesses with LLM-as-judge and regression gates (data)
  - `data-quality-validator` — expectation suites for tables and pipelines (data)
  - `feature-engineering-assistant` — leakage-safe ML feature design and pipelines (data)
  - `webhook-integration-builder` — signed, idempotent, retry-safe webhook producers/consumers (development)
  - `api-versioning-strategist` — versioning strategy, deprecation timelines, and migration guides (development)
  - `legacy-code-modernizer` — incremental strangler-fig modernization with characterization tests (development)
  - `iam-policy-reviewer` — least-privilege review of cloud IAM policies (security)
  - `secrets-scanner` — detect and remediate leaked credentials in code and git history (security)
  - `release-notes-writer` — audience-appropriate release notes from PRs and commits (writing)
  - `grant-proposal-writer` — structured, funder-aligned grant proposals (research)
  - `product-requirements-writer` — PRDs with goals, acceptance criteria, and open questions (productivity)
  - `sprint-retro-facilitator` — action-oriented retrospective synthesis (productivity)
  - `storyboard-generator` — shot-by-shot storyboards with image prompts (creative)

### Changed

- Total skills: 120 (from 103)

## [0.2.0] - 2026-06-24

### Added

- 10 new skills across 6 categories:
  - `multi-agent-orchestrator` — coordinator/specialist agent system design with routing and verification (development)
  - `dependency-upgrader` — safe, sequenced dependency upgrades with code migrations (development)
  - `dockerfile-optimizer` — smaller, faster, more secure Docker images (ops)
  - `helm-chart-generator` — package Kubernetes apps as reusable Helm charts (ops)
  - `incident-postmortem-writer` — blameless postmortems from incident notes (ops)
  - `cohort-analysis` — retention and behavioral cohort analysis (data)
  - `synthetic-data-generator` — statistically faithful, privacy-safe synthetic datasets (data)
  - `market-research-analyst` — market sizing, competitor matrices, and SWOT briefs (research)
  - `meeting-agenda-planner` — focused, time-boxed meeting agendas (productivity)
  - `voice-ui-script-writer` — conversational scripts and dialog flows for voice/IVR (creative)

### Changed

- Total skills: 103 (from 93)

## [0.1.9] - 2026-06-19

### Added

- 11 new skills across 6 categories:
  - `rag-pipeline-builder` — end-to-end retrieval-augmented generation pipeline design (data)
  - `chart-generator` — data visualization and chart-rendering code generation (data)
  - `data-anonymizer` — PII detection and redaction with privacy-preserving techniques (security)
  - `prompt-injection-tester` — LLM red-teaming for prompt injection and jailbreaks (security)
  - `database-migration-writer` — safe, reversible zero-downtime schema migrations (development)
  - `code-comment-generator` — docstrings and inline comments for existing code (development)
  - `api-mock-server` — mock API servers and stubbed responses from specs (testing)
  - `feature-flag-manager` — feature flagging and progressive-delivery strategies (ops)
  - `seo-content-optimizer` — on-page SEO optimization and structured data (writing)
  - `localization-helper` — i18n/l10n extraction and translation (writing)
  - `customer-support-responder` — grounded, empathetic support replies and macros (productivity)

### Changed

- Total skills: 93 (from 82)

## [0.1.8] - 2026-06-12

### Added

- 7 new skills across 4 categories:
  - `kubernetes-manifest-generator` — production-ready K8s manifests, Kustomize/Helm scaffolding (ops)
  - `log-analysis` — log parsing, anomaly detection, and root-cause analysis (ops)
  - `graphql-schema-generator` — GraphQL SDL, resolvers, and pagination design (development)
  - `meeting-notes-summarizer` — structured summaries with decisions and action items (productivity)
  - `pdf-data-extraction` — structured data extraction from PDFs and scanned documents (data)
  - `sentiment-analysis` — document-level and aspect-based sentiment classification (data)
  - `user-story-writer` — agile user stories with Gherkin acceptance criteria (productivity)

### Changed

- Total skills: 82 (from 75)

## [0.1.7] - 2026-06-04

### Added

- 10 new skills across 7 categories:
  - `infrastructure-as-code` — Terraform/CDK/Pulumi IaC generation (ops)
  - `threat-modeling` — STRIDE analysis and security threat assessment (security)
  - `video-analysis` — video content analysis with scene detection and annotation (data)
  - `api-load-testing` — k6/Locust load testing script generation (testing)
  - `audio-transcription` — audio transcription with speaker diarization (productivity)
  - `contract-analysis` — legal contract review and risk assessment (research)
  - `incident-response` — SRE runbooks and postmortem generation (ops)
  - `mobile-app-prototyping` — SwiftUI/Compose/React Native prototyping (development)
  - `design-system-generator` — design tokens and component specifications (creative)
  - `data-pipeline-builder` — Airflow/dbt/Spark ETL pipeline generation (data)

### Changed

- Total skills: 75 (from 66)

## [0.1.5] - 2026-05-31

### Added

- 4 new App Store Optimization (ASO) skills inspired by [Eronred/aso-skills](https://github.com/Eronred/aso-skills):
  - `aso-audit` — full ASO health check with 10-dimension scored report card (0–100), quick wins, and prioritized action plan
  - `aso-competitor-analysis` — competitive intelligence: keyword gaps, creative strategy, ratings, monetization, and growth signals
  - `aso-keyword-research` — keyword discovery, opportunity scoring (volume × difficulty × relevance), and strategy bucketing
  - `aso-metadata-optimization` — title, subtitle, keyword field, and description writing with iOS/Android platform-specific rules

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
