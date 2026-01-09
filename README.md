# Articles tecnics en Markdown

Aquest repositori es un boilerplate per escriure articles en Markdown en catala,
crear la versio en angles, i publicar-los a dev.to i a GitHub Pages.

## Estructura

- `content/ca/`: fonts en catala (amb front matter).
- `content/en/`: traduccions en angles (amb front matter).
- `output/`: lloc web generat per Pelican (per a GitHub Pages).
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

Segueix `TRANSLATION.md` per fer la traduccio amb un agent.

4. Exportar per a dev.to:

```
uv run scripts/export_devto.py
```

## Tooling (Python)

- `pre-commit`: hooks de format i lint.
- `ruff`: lint per a scripts.
- `mdformat`: format Markdown.
- `pelican`: generador de llocs estatics per al blog.

Instal.lacio suggerida:

```
uv sync
uvx pre-commit install
```

## GitHub Pages

Edita `pelicanconf.py` i actualitza `SITENAME` i altres configuracions.

Per construir el site:

```
uv run pelican content
```

Per servir-lo localment:

```
uv run pelican --listen
```

## Nox

```
uv run nox -s lint
uv run nox -s format
uv run nox -s docs
```
