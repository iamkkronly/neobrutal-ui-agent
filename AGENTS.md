# AGENTS.md — Neo Brutalism UI contract

This repository is a design instruction set for AI coding agents. Apply these rules to every UI you create here.

## Prime directive

**Always use Neo-Brutalism as the primary visual language.** Do not replace it with a generic SaaS, soft-minimal, neumorphic, or gradient-heavy look.

## Required baseline

- Use thick, visible, near-black borders on interactive surfaces.
- Use hard offset shadows; never default to blurred drop shadows.
- Prefer flat, high-contrast color blocks over gradients.
- Use a warm off-white canvas and a small, intentional accent palette.
- Make hierarchy obvious with large display typography, compact labels, and clear spacing.
- Keep controls keyboard accessible, focus-visible, and readable at WCAG AA contrast.
- Design responsive layouts from the content outward; do not hide essential actions on mobile.
- Reuse the tokens in `design-system/tokens/` before adding new values.

## Supporting style rules

- **Typography:** expressive and oversized where useful, but never at the expense of readable body text.
- **Retro Pixel Art:** optional accent for icons, stickers, avatars, empty states, or decorative marks. Do not make the entire UI pixelated unless the brief explicitly asks for it.
- **Claymorphism:** optional, rare, and limited to a tactile/friendly component. Keep a hard border and brutalist layout around it.
- **Glassmorphism:** exceptional and limited to overlays that genuinely need background context. Never use frosted glass as the page background or default card style.

## Implementation rules

1. Inspect the existing structure before changing it.
2. Read `agent/design-contract.md` and the relevant component recipe.
3. Prefer semantic HTML and native controls.
4. Use CSS variables from `design-system/tokens/css-tokens.css`.
5. Add states: default, hover, active, focus-visible, disabled, and error where relevant.
6. Validate with `python3 scripts/validate.py` before finishing.
7. Do not add a new visual trend unless the user explicitly asks for it and the change is documented.

## Decision test

Before accepting a visual choice, ask:

> If the decorative accent disappeared, would the interface still clearly read as Neo-Brutalist?

If the answer is no, remove or reduce the accent.
