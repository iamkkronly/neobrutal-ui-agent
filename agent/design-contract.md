# Design contract for AI-generated UI

## Mission

Create interfaces that feel direct, confident, expressive, and easy to operate. Every screen should look intentionally Neo-Brutalist before any supporting accent is added.

## 1. Style priority

Apply the following priority order:

1. Accessibility, semantics, and task clarity.
2. Neo-Brutalist structure: hard borders, flat color, offset shadows, visible grid.
3. Typography: clear hierarchy and expressive but readable type.
4. Retro Pixel Art: small, purposeful character.
5. Claymorphism: a rare tactile accent.
6. Glassmorphism: an exceptional contextual overlay.

If a lower-priority style conflicts with a higher-priority rule, remove the lower-priority style.

## 2. Color system

Start with `--color-paper` and `--color-ink`. Add one or two accents from yellow, pink, blue, green, or orange. Use ink for text and borders. Check contrast for every text/background pair; do not rely on the colors looking bright enough.

Color should encode hierarchy or state, not fill every surface. Keep error states distinguishable by text or iconography as well as red.

## 3. Shape, depth, and layout

- Default corner radius is zero or small (`--radius-sm`).
- A larger radius requires a functional reason, not trend-following.
- Use `--shadow-sm`, `--shadow-md`, or `--shadow-lg`; never make a blurred shadow the primary depth cue.
- Expose the layout: use an intentional grid, alignment, and strong section boundaries.
- Use full-bleed color blocks, stickers, labels, and offsets sparingly to create rhythm.
- Preserve a usable content width and do not make asymmetry destroy scanning order.

## 4. Typography

- Display: bold, compact, and allowed to be oversized for a hero or key metric.
- Body: system sans-serif or an equally readable sans-serif, with comfortable line height.
- Labels: monospace or uppercase only when it improves metadata scanning.
- Avoid setting entire paragraphs in uppercase or pixel fonts.
- Keep a clear type scale with no more than three dominant sizes on one screen.

## 5. Accent recipes

### Retro Pixel Art

Use blocky icons, pixel corners, or a tiny decorative sprite. Keep it legible at the target size and provide a text alternative for meaningful content. Never turn a data-dense product into an unreadable pixel-art poster.

### Claymorphism

A clay-like element may use a soft inner highlight or rounded geometry when the metaphor is useful. It still needs an ink boundary or an adjacent brutalist frame. Do not use clay styling for every surface.

### Glassmorphism

Reserve translucent backgrounds, backdrop blur, and fine hairline highlights for a temporary overlay, floating inspector, or layer where the background context matters. The overlay still needs a strong focus order, solid fallback background, and readable contrast when blur is unavailable.

## 6. Interaction and accessibility

- Use semantic landmarks: header, nav, main, section, footer.
- Keep keyboard focus visible and never remove the browser focus indicator without replacing it.
- Minimum target size: 44 × 44 px for touch controls.
- Respect `prefers-reduced-motion`.
- Include hover, active, focus-visible, disabled, loading, empty, error, and success states when relevant.
- Make status changes available to assistive technology with appropriate live regions.
- Do not communicate meaning with color alone.

## 7. Responsive behavior

Design the smallest useful layout first. On narrow screens:

- Stack grids and preserve reading order.
- Let typography wrap; do not force horizontal scrolling for ordinary content.
- Keep the primary action visible.
- Reduce shadow offsets if they cause clipping, but retain the hard-shadow character.
- Move decorative pixels out of the content path.

## 8. Delivery format

When generating a new feature, provide:

1. A short design rationale explaining how Neo-Brutalism remains primary.
2. Semantic markup and token-based styling.
3. All relevant interaction states.
4. A responsive behavior note.
5. A brief accessibility check.
6. Validation results from `python3 scripts/validate.py`.

## 9. Anti-patterns

Reject a screen if it is primarily:

- a generic white dashboard with subtle gray borders;
- a gradient-first marketing page;
- a collection of soft floating cards;
- a glass panel wall;
- an all-pixel novelty that weakens readability;
- a visual collage where each component uses a different trend.
