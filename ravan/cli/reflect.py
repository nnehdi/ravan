import rich
import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main():
    rich.print("What's in your mind?")
