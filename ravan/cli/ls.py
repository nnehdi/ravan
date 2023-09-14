import typer
from rich import print
from typing_extensions import Annotated

from ravan.storage.journal_session_storage import JournalSessionStorage
from ravan.storage.storage_engine import StorageEngine

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(
    limit: Annotated[
        int, typer.Option("-l", "--limit", help="Number of entries to show.")
    ] = 10,
    offset: Annotated[
        str, typer.Option("-o", "--offset", help="Number of entries to skip.")
    ] = 0,
    interactive: Annotated[
        bool,
        typer.Option(
            "--interactive",
            "-i",
            help="Start the an interactive shell. \
            You can work directly with datamodel using SQLModel",
        ),
    ] = False,
):
    if interactive:
        # import needed for the convenient use
        storage = StorageEngine()  # noqa: F841
        import IPython
        from sqlmodel import select  # noqa: F401

        from ravan.storage.models import Chat, JournalSession, Message  # noqa: F401

        IPython.embed()
        typer.Exit()
    storage = JournalSessionStorage()
    print("Reflections:")
    reflections = storage.get_all_sessions(limit, offset)
    for reflection in reflections:
        first_user_msg = "No messages"
        if len(reflection.chat.messages) >= 3:
            first_user_msg = reflection.chat.messages[2].content.strip()
        print(
            f"{reflection.id}. {reflection.created_at}: \
            {first_user_msg[:75]+'...' if len(first_user_msg) > 75 else first_user_msg}"
        )
    print("To dive deeper into a specific reflection, use: ravan view <id>")
