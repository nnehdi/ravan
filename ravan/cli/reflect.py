import typer
from rich.prompt import Prompt

from ravan.llm.chat import Chat
from ravan.storage.journal_session_storage import JournalSessionStorage

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main():
    system_prompt = """
    You are a smart personal journal that helps users with guided reflectoins.
    You start by giving user a prompt as  a starting point for their reflection.
    Then you listen to their response and curate the next prompt based on their response
    """
    chat = Chat(system_prompt)

    storage = JournalSessionStorage()
    storage.init_journal_session()
    res = chat.chat()
    while True:
        user_input = Prompt.ask(res + "\n")
        if user_input in [":q", ":quit", ":exit"]:
            break
        res = chat.chat(user_input)
