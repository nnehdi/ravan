import pytest

from ravan.storage.journal_session_storage import JournalSessionStorage
from ravan.storage.storage_engine import StorageEngine


@pytest.fixture()
def memory_engine():
    engine = StorageEngine(db_uri="sqlite:///:memory:")
    engine.init_storage()
    return engine


# TODO test if table is created
def test_if_tables_are_created(memory_engine):
    pass


def test_init_journal_session_storage(memory_engine):
    storage = JournalSessionStorage(memory_engine)
    journal_session = storage.init_journal_session()
    session_id = journal_session.id
    assert session_id is not None


def test_add_message(memory_engine):
    storage = JournalSessionStorage(memory_engine)
    journal_session = storage.init_journal_session()
    msg = storage.add_message(journal_session.id, "usre", "test message")
    return msg.id is not None
