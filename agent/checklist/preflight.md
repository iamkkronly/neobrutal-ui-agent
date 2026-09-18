# UI preflight checklist

## Design

- [ ] Neo-Brutalism is visibly the primary visual language.
- [ ] Borders are visible and shadows are hard, not blurred.
- [ ] The palette uses tokens and has a clear contrast hierarchy.
- [ ] Supporting accents are purposeful and limited.
- [ ] Typography establishes hierarchy without sacrificing readability.

## Product quality

- [ ] The primary user action is obvious.
- [ ] Empty, loading, error, success, hover, active, disabled, and focus states exist where relevant.
- [ ] Mobile layout preserves content order and essential actions.
- [ ] Decorative elements do not compete with the task.

## Accessibility

- [ ] Semantic landmarks and native controls are used.
- [ ] Keyboard navigation works and focus-visible is obvious.
- [ ] Text/background contrast is checked.
- [ ] Color is not the only signal.
- [ ] Reduced motion is respected.
- [ ] Touch targets are at least 44 px where applicable.

## Engineering

- [ ] Existing patterns were reused before adding new ones.
- [ ] No secrets or tokens were added to the repository.
- [ ] `python3 scripts/validate.py` passes.
