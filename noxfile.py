import nox


@nox.session
def lint(session: nox.Session) -> None:
    session.install("-r", "requirements-dev.txt")
    session.run("ruff", "check", "scripts", "noxfile.py")


@nox.session
def format(session: nox.Session) -> None:
    session.install("-r", "requirements-dev.txt")
    session.run(
        "mdformat",
        "README.md",
        "docs",
        "content",
        "templates",
        "TRANSLATION.md",
    )
    session.run("ruff", "format", "scripts", "noxfile.py")


@nox.session
def docs(session: nox.Session) -> None:
    session.install("-r", "requirements.txt")
    session.run("mkdocs", "build")


@nox.session
def serve(session: nox.Session) -> None:
    session.install("-r", "requirements.txt")
    session.run("mkdocs", "serve", "-a", "127.0.0.1:8000")
