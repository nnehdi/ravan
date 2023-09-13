from typing import Optional

import typer

from ravan import __app_name__, __version__
from ravan.cli import ls, reflect

app = typer.Typer()
app.add_typer(reflect.app, name="reflect")
app.add_typer(ls.app, name="ls")


def _version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback(invoke_without_command=True)
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
):
    pass
