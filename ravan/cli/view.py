import typer
from rich import print
from typing_extensions import Annotated

from ravan.storage.journal_session_storage import JournalSessionStorage

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(id: Annotated[int, typer.Argument(help="The id of the entry to be viewed.")]):
    journal_session_storage = JournalSessionStorage()
    journal_session = journal_session_storage.get_session(id)
    print(journal_session.created_at)
    for message in journal_session.chat.messages[1:]:
        print(f"<{message.role}> \n{message.content}")
