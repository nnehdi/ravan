from datetime import datetime

from sqlmodel import select

from ravan.helpers.singleton import SingletonMeta
from ravan.storage.models import Chat, JournalSession, Message
from ravan.storage.storage_engine import StorageEngine


class JournalSessionStorage(metaclass=SingletonMeta):
    def __init__(self, storage_engine=None) -> None:
        if not storage_engine:
            storage_engine = StorageEngine()
        self._engine = storage_engine
        self._journal_session = None
        self._chat = None

    def init_journal_session(self):
        with self._engine.session() as session:
            journal_session = JournalSession()
            chat = Chat(session=journal_session)
            session.add(chat)
            session.commit()
            session.refresh(journal_session)
            session.refresh(chat)
            self._journal_session = journal_session
            self._chat = chat
            return journal_session

    def add_message(self, content, role, created_at=None):
        if not created_at:
            created_at = datetime.now()
        with self._engine.session() as session:
            message = Message(
                content=content, role=role, chat=self._chat, created_at=created_at
            )
            session.add(message)
            session.commit()
            session.refresh(message)
            return message

    def get_all_sessions(self, limit=10, offset=0):
        with self._engine.session() as session:
            statement = select(JournalSession).limit(limit).offset(offset)
            return session.exec(statement).unique().all()
