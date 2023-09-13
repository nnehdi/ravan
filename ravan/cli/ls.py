from typing import Optional

import typer

from ravan.storage.storage_engine import StorageEngine

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(
    shell: Optional[bool] = typer.Option(
        False,
        "--interactive",
        "-i",
        help="Start the an interactive shell. \
            You can work directly with datamodel using SQLModel",
    )
):
    if shell:
        # import needed for the convenient use
        storage = StorageEngine()  # noqa: F841
        import IPython
        from sqlmodel import select  # noqa: F401

        from ravan.storage.models import Chat, JournalSession, Message  # noqa: F401

        IPython.embed()

    pass
