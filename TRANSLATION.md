# Translation workflow

Goal: keep Catalan as the source of truth in `content/ca/` and produce English in
`content/en/`.

## Suggested flow with Codex

1. Generate a stub in English:

```
uv run scripts/prepare_translation.py --slug <slug>
```

2. Ask Codex to translate the body. Example prompt:

```
Translate this article from Catalan to English. Keep the Markdown structure,
code blocks, and lists. Do not translate code or command examples. Keep the
front matter but translate title/description and tags if needed.

<PASTE THE CONTENT OF content/ca/<slug>.md HERE>
```

3. Paste the translated result into `content/en/<slug>.md` and review.

1. Run:

```
uv run scripts/render_docs.py
uv run scripts/export_devto.py
```
