from sqlmodel import Session, SQLModel, create_engine

from ravan.config import Config
from ravan.helpers.singleton import SingletonMeta


class StorageEngine(metaclass=SingletonMeta):
    def __init__(self, db_uri=None) -> None:
        if not db_uri:
            sqlite_filename = Config.SQLITE_FILEPATH
            db_uri = f"sqlite:///{sqlite_filename}"
        self._engine = create_engine(db_uri)

    def init_storage(self):
        SQLModel.metadata.create_all(self._engine)

    def session(self):
        return Session(self._engine)
