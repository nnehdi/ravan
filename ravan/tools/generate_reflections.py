import json
import os

from dotenv import find_dotenv, load_dotenv
from langchain.llms import OpenAI
from rich import print

from ravan.storage.journal_session_storage import JournalSessionStorage

PROMPT = """
Generate a reflective conversation between a smart personal journal AI and a user.\
      The conversation structure should adhere to this pattern:
Start with a general reflection prompt from the AI.
2. Include a hypothetical user's response.
3. Follow with the AI curating a deeper reflection prompt based on the user's reply.
4. Continue a long conversation between the user and AI back and forth more than 20 \
    times.
5. Conclude with a final reflective user response.

Ensure the AI prompts are:
- Easy to understand.
- Concise and short.
- Hints are surrounded by brackets [] to guide the user's thought process.

The output should a valid json format as follow:

{"data":[
    {
        "role": "ai",
        "content": "Think about a recent event that made an impact on you.What was it?",
        "hint": "It could be a personal achievement, an interaction with someone,\
              or even a simple observation."
    },
    {
        "role": "user",
        "content": "I recently traveled solo for the first time."
    },
    {
        "role": "ai",
        "content": "Traveling alone can be a transformative experience. \
            What feelings surfaced during this solo trip?",
        "hint": "Consider moments of independence, loneliness, or even unexpected joys."
    },
    {
        "role": "user",
        "content": "At first, I felt a mix of anxiety and excitement.\
              But as days passed, I felt a deep sense of freedom and self-discovery."
    }
]}

THE AI MESSAGE SHOULD ALWAYS HAVE A `hint` FILED
DON'T COMPLETE THIS CONVERSATION, START THE WHOLE NEW CONVERSATION
"""


def generate_reflection():
    load_dotenv(find_dotenv())
    llm = OpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo-instruct",
        max_tokens=3700,
    )
    json_string = llm(PROMPT)
    return json.loads(json_string)


def generate_reflections(count=5):
    for i in range(count):
        sample = generate_reflection()
        print(f"Reflection {i+1}")
        print(sample["data"])
        journal_storage = JournalSessionStorage()
        journal_storage.init_journal_session()
        # here we add the first system prompt as we do with manually created session
        from ravan.cli.reflect import SYSTEM_PROMPT

        journal_storage.add_message(SYSTEM_PROMPT, "system")
        for msg in sample["data"]:
            if msg["role"] == "ai":
                msg["content"] = f"{msg['content']} \nHint: {msg['hint']}"
            journal_storage.add_message(msg["content"], msg["role"])
        print(f"reflection {i+1} has been successfully inserted into the db")


if __name__ == "__main__":
    count = 10
    print(f"Generating {count} reflections")
    generate_reflections(count)
