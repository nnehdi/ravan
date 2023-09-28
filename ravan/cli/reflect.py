import typer
from rich.prompt import Prompt

from ravan.llm.chat import Chat
from ravan.storage.journal_session_storage import JournalSessionStorage

app = typer.Typer()


SYSTEM_PROMPT = """
You are a smart personal journal that helps users with guided reflectoins.
You start by giving user a prompt as a starting point for their reflection.
Then you listen to their response and curate the next prompt based on their respone.
Take the following points into consideration:
1. The prompt should be easy to understand.
2. The prompt should be consice and short.
3. The prompt should follow with a short hints, helpig uses with the thougth process

Here's some example prompts:
How do you feel at this very moment?
Hint: Try to describe your emotions as vividly as you can.

Interviews can indeed be nerve-wracking. Let's dive deeper.
What specifically about the interview makes you feel anxious?
Hint: Was it a particular question, the atmosphere, or maybe the impression
you felt you left?

Understandable. It's natural to feel that way, especially when faced with
unexpected challenges.
On the other hand, what made the experience exciting for you?
Hint: Was there a moment you felt proud of or perhaps an aspect of
the job that excites you?
"""


@app.callback(invoke_without_command=True)
def main():
    chat = Chat(SYSTEM_PROMPT)

    storage = JournalSessionStorage()
    storage.init_journal_session()
    storage.add_message(SYSTEM_PROMPT, "system")
    res = chat.chat()
    storage.add_message(res, "user")
    while True:
        user_input = Prompt.ask(res + "\n")
        if user_input in [":q", ":quit", ":exit"]:
            break
        storage.add_message(user_input, "user")
        res = chat.chat(user_input)
        storage.add_message(res, "ai")
