# Contributing to OpenModels Skills

Thanks for contributing! This guide covers how to add new skills to the registry.

## Adding a New Skill

### 1. Create the YAML file

Create `skills/{skill-id}.yaml` where `{skill-id}` matches the `id` field inside the file.

**Naming rules:**
- Use kebab-case: lowercase alphanumeric with hyphens
- Pattern: `^[a-z0-9]+(-[a-z0-9]+)*$`
- Be descriptive but concise (e.g., `code-review`, not `cr`)

### 2. Fill in required fields

Every skill must include:

| Field | Description |
|-------|-------------|
| `id` | Unique kebab-case identifier (must match filename) |
| `name` | Human-readable display name |
| `description` | What the skill does and when to use it (10-2000 chars) |
| `category` | One of: development, writing, data, research, creative, ops, testing, security, productivity |
| `tags` | 1-20 searchable tags in kebab-case |
| `author` | Object with `name` (required), `github` and `url` (optional) |
| `recommended_models` | Model IDs from the OpenModels registry that work well |
| `modalities` | Object with `input` and `output` arrays (text, image, audio, video, code, file) |
| `complexity` | One of: beginner, intermediate, advanced |
| `use_cases` | 1-10 concrete use cases (5-500 chars each) |
| `example_prompt` | A ready-to-use prompt template (10-5000 chars) |
| `created_at` | ISO 8601 timestamp |
| `updated_at` | ISO 8601 timestamp |

### 3. Optional fields

| Field | Description |
|-------|-------------|
| `source_url` | Link to source code or extended documentation |
| `min_context_window` | Minimum tokens needed (1000-10000000) |
| `related_skills` | IDs of related skills for discovery |
| `compatible_tools` | AI tools this works with (claude-code, cursor, kiro, etc.) |

### 4. Validate

```bash
pip install -r requirements.txt
python validate.py
```

### 5. Submit a PR

- One skill per PR (easier to review)
- Include a brief description of the skill's purpose
- If referencing models in `recommended_models`, ensure they exist in the main OpenModels registry

## Quality Guidelines

Good skills are:

- **Specific** — actionable steps, not vague advice
- **Verifiable** — clear expected outputs
- **Model-aware** — recommend appropriate models for the task complexity
- **Well-prompted** — the `example_prompt` should be immediately usable
- **Connected** — link to related skills for discovery

## Example Prompt Tips

The `example_prompt` field is the most important part for users. Make it:

1. **Self-contained** — include placeholders like `[paste code here]`
2. **Structured** — use numbered lists for multi-part requests
3. **Specific about output format** — tell the model what deliverables you expect
4. **Realistic** — based on actual workflows, not toy examples

## Categories

Choose the most specific category:

- `development` — writing and improving code
- `writing` — generating text content (docs, emails, copy)
- `data` — analysis, SQL, visualization
- `research` — information gathering and synthesis
- `creative` — brainstorming, ideation
- `ops` — CI/CD, infrastructure, deployment
- `testing` — test generation, QA
- `security` — auditing, vulnerability detection
- `productivity` — workflow automation, git, tooling

## Complexity Levels

- `beginner` — works well with smaller/faster models, simple tasks
- `intermediate` — needs capable models, multi-step reasoning
- `advanced` — requires top-tier models, complex analysis, large context

## Model Recommendations

When choosing `recommended_models`:

- Reference model IDs from the [OpenModels registry](https://github.com/openmodelsrun/openmodels)
- Include 2-5 models that genuinely work well for the task
- Consider different tiers (a flagship model + a cost-effective alternative)
- Test your example prompt with the recommended models if possible

## Code of Conduct

Be respectful, constructive, and inclusive. We're building a community resource.
