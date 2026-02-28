import os

import typer
from dotenv import find_dotenv, load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from rich import print
from typing_extensions import Annotated

from ravan.storage.journal_session_storage import JournalSessionStorage

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main(
    query: Annotated[
        str, typer.Argument(help="a question over your reflections to get an insight")
    ]
):
    print(f"Processing your query: {query}")
    storage = JournalSessionStorage()
    reflections = storage.get_all_sessions(limit=5)
    documents = list()
    for reflection in reflections:
        messages = [
            f"{msg.role}: {msg.content}" for msg in reflection.chat.messages[1:]
        ]
        doc = Document(
            page_content="\n".join(messages), metadata={"session_id": reflection.id}
        )
        documents.append(doc)

    # Get your splitter ready
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=50)

    # Split your docs into texts
    texts = text_splitter.split_documents(documents)
    # Get embedding engine ready
    load_dotenv(find_dotenv())
    OPEN_AI_KEY = os.getenv("OPENAI_API_KEY")
    embeddings = OpenAIEmbeddings(openai_api_key=OPEN_AI_KEY)
    llm = OpenAI(openai_api_key=OPEN_AI_KEY)
    # Embedd your texts
    db = FAISS.from_documents(texts, embeddings)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=db.as_retriever(),
        return_source_documents=True,
        verbose=True,
    )
    result = qa({"query":query, "verbose":True})
    print(result["source_documents"])
    print(result["result"])
