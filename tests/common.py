import pytest

from ravan.storage.journal_session_storage import JournalSessionStorage
from ravan.storage.storage_engine import StorageEngine


@pytest.fixture()
def memory_engine(mocker):
    mem_engine = StorageEngine(db_uri="sqlite:///:memory:")
    mem_engine.init_storage()
    fake_engine = mocker.patch("ravan.storage.storage_engine.StorageEngine")
    fake_engine.return_value = memory_engine
    return mem_engine


@pytest.fixture()
def create_one_session(memory_engine):
    storage = JournalSessionStorage(memory_engine)
    journal_session = storage.init_journal_session()
    return journal_session
