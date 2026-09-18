# Neo Brutalism UI

A design contract and starter kit for AI agents that build bold, useful interfaces.

> **Default rule:** build in Neo-Brutalism first. Retro Pixel Art, expressive Typography, Claymorphism, and Glassmorphism are supporting accents—not competing visual systems.

## What this repository does

Give an AI coding agent this repository (or point it at the repository name) and it gets a reusable visual contract for generating interfaces:

- **Neo-Brutalism is the non-negotiable base:** hard black borders, offset shadows, high contrast, flat surfaces, visible structure, and confident color blocks.
- **Typography has a job:** oversized display text, tight hierarchy, readable body copy, and deliberate label styles.
- **Retro Pixel Art is an accent:** use for icons, tiny illustrations, badges, empty states, and decorative details when the product benefits from it.
- **Claymorphism is optional:** only for a friendly, tactile component where depth improves comprehension; keep the outer layout brutalist.
- **Glassmorphism is exceptional:** only for overlays or translucent layers that need context behind them; never use it as the main page aesthetic.

## Start here for an AI agent

Read these files in order:

1. [`AGENTS.md`](AGENTS.md) — short, mandatory implementation rules.
2. [`agent/design-contract.md`](agent/design-contract.md) — the full visual and interaction contract.
3. [`design-system/tokens/css-tokens.css`](design-system/tokens/css-tokens.css) — copy the tokens before inventing values.
4. [`agent/checklist/preflight.md`](agent/checklist/preflight.md) — quality gate before shipping.
5. [`agent/prompts/generate-ui.md`](agent/prompts/generate-ui.md) — prompt template for new screens.

## Preview the demo

No build step is required:

```bash
python3 -m http.server 8080 --directory demos
```

Then open <http://localhost:8080>.

## Repository map

```text
AGENTS.md                         machine-readable design directive
agent/design-contract.md          detailed rules for humans and AI agents
agent/checklist/preflight.md      review checklist
agent/prompts/generate-ui.md      reusable generation prompt
design-system/tokens/             source-of-truth design tokens
design-system/themes/             theme boundaries and accent guidance
design-system/components/         component behavior and styling recipes
demos/                            dependency-free reference implementation
docs/                             decisions and rationale
scripts/                          lightweight validation tools
```

## The hierarchy of decisions

When a new request is ambiguous, resolve it in this order:

1. **Usability and accessibility**
2. **Neo-Brutalist structure and contrast**
3. **Typography and content hierarchy**
4. **Retro Pixel Art accents when they add character**
5. **Claymorphism or Glassmorphism only when the component's purpose calls for it**

Do not mix every style into every component. A coherent Neo-Brutalist product with one purposeful accent is better than a collage of trends.

## License

MIT. See [`LICENSE`](LICENSE).
