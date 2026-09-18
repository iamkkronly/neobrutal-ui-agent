#!/usr/bin/env python3
"""Small dependency-free repository quality checks."""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    "README.md",
    "AGENTS.md",
    "agent/design-contract.md",
    "agent/checklist/preflight.md",
    "agent/prompts/generate-ui.md",
    "design-system/tokens/core.json",
    "design-system/tokens/css-tokens.css",
    "demos/index.html",
    "demos/assets/css/style.css",
    "demos/assets/js/app.js",
]
errors = []
for relative in required:
    path = ROOT / relative
    if not path.is_file() or not path.read_text(encoding="utf-8").strip():
        errors.append(f"missing or empty: {relative}")

try:
    tokens = json.loads((ROOT / "design-system/tokens/core.json").read_text(encoding="utf-8"))
    for key in ("color", "font", "space", "shadow"):
        if key not in tokens:
            errors.append(f"tokens missing key: {key}")
except (OSError, json.JSONDecodeError) as exc:
    errors.append(f"invalid token JSON: {exc}")

text_files = [ROOT / "README.md", ROOT / "AGENTS.md", ROOT / "agent/design-contract.md"]
for path in text_files:
    text = path.read_text(encoding="utf-8")
    if "Neo-Brutalism" not in text:
        errors.append(f"design language not declared in: {path.relative_to(ROOT)}")

# Never commit credentials or local token artifacts.
for path in ROOT.rglob("*"):
    if path.is_file() and path.name in {".ghtoken", ".env", ".env.local"}:
        errors.append(f"secret-like file inside repository: {path.relative_to(ROOT)}")

if errors:
    print("VALIDATION FAILED")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print(f"VALIDATION PASSED — {len(required)} required files checked")
