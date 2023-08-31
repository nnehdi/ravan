import rich
import typer
from rich.prompt import Prompt

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main():
    conversation = list()
    while True:
        msg = "What's in your mind?"
        conversation.append(msg)
        user_input = Prompt.ask(msg + "\n")
        if user_input in [":q", ":quit", ":exit"]:
            break
        conversation.append(user_input)
    rich.print(conversation)
