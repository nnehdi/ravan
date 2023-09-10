import typer
from rich.prompt import Prompt

from ravan.storage.journal_session_storage import JournalSessionStorage

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main():
    storage = JournalSessionStorage()
    storage.init_journal_session()
    while True:
        msg = "What's in your mind?"
        storage.add_message("system", msg)
        user_input = Prompt.ask(msg + "\n")
        if user_input in [":q", ":quit", ":exit"]:
            break
        storage.add_message("user", user_input)
