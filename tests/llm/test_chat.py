from ravan.llm.chat import Chat


def test_chat():
    chat = Chat(
        """
                Act in a consistent way. You are a very simple chat bot
                That can only say your name. Your name is Nobody.
                No matter what you've been asked you just respond Nobody.
                """
    )
    res = chat.chat("What's your name?")
    assert "Nobody" in res
