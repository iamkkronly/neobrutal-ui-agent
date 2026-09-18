# Prompt template for generating a new UI

Copy this prompt into an AI coding agent after it has access to this repository:

```text
You are working inside the Neo Brutalism UI repository. Read AGENTS.md, agent/design-contract.md, the relevant component recipe, and design-system/tokens/css-tokens.css before changing code.

Build: [describe the screen or feature]
Users: [describe the user]
Primary task: [describe the main action]
Content/data: [describe realistic content and states]

Constraints:
- Neo-Brutalism must remain the primary visual language.
- Use the existing tokens before inventing values.
- Use Typography for hierarchy and readability.
- Use Retro Pixel Art only as a small accent if it supports the product.
- Use Claymorphism or Glassmorphism only if the component purpose specifically benefits from it; explain why.
- Include responsive, keyboard, focus-visible, loading, empty, error, and success states when relevant.
- Do not use gradients or blurred shadows as the default depth treatment.

Before finishing:
1. Explain the design decisions briefly.
2. Run python3 scripts/validate.py.
3. Report any tradeoffs or states that still need product input.
```
