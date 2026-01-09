# Articles tecnics en Markdown

Aquest repositori es un boilerplate per escriure articles en Markdown en catala,
crear la versio en angles, i publicar-los a dev.to i a GitHub Pages.

## Estructura

- `content/ca/`: fonts en catala (amb front matter per dev.to).
- `content/en/`: traduccions en angles (amb front matter per dev.to).
- `docs/`: sortida per a GitHub Pages (renderitzada des de `content/`).
- `exports/devto/`: fitxers preparats per pujar a dev.to.
- `scripts/`: utilitats en Python.
- `templates/`: plantilles d'article.

## Flux de treball recomanat

1. Crear un article nou:

```
uv run scripts/new_article.py --lang ca --slug el-meu-article --title "El meu article"
```

2. Escriure l'article a `content/ca/el-meu-article.md`.

1. Generar la versio anglesa (manual + assistent):

```
uv run scripts/prepare_translation.py --slug el-meu-article
```

Segueix `TRANSLATION.md` per fer la traduccio amb un agent (ex: Codex).

4. Renderitzar per a GitHub Pages:

```
uv run scripts/render_docs.py
```

5. Exportar per a dev.to:

```
uv run scripts/export_devto.py
```

## Tooling (Python)

- `pre-commit`: hooks de format i lint.
- `ruff`: lint per a scripts.
- `mdformat`: format Markdown.
- `mkdocs` + `mkdocs-material`: site per a GitHub Pages.

Instal.lacio suggerida:

```
uv sync
uvx pre-commit install
```

## GitHub Pages

Edita `mkdocs.yml` i actualitza `site_url` amb la teva URL real.

Per construir el site:

```
uv run mkdocs build
```

Per servir-lo localment:

```
uv run mkdocs serve
```

## Nox

```
uv run nox -s lint
uv run nox -s format
uv run nox -s docs
```
