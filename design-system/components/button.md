# Button recipe

Use a native `<button>` whenever the action changes state. Use a link for navigation.

```html
<button class="btn btn--primary" type="button">Save changes</button>
```

Required states:

- Default: 3 px ink border, colored flat fill, hard offset shadow.
- Hover: increase or shift the shadow; do not introduce blur.
- Active: translate toward the shadow and reduce shadow to `--shadow-pressed`.
- Focus-visible: add a clear 3 px outline with a 3 px offset.
- Disabled: reduce contrast only enough to signal unavailable state; keep text readable.

Keep labels action-oriented. Avoid pill-shaped buttons unless the pill communicates a compact status rather than an action.
