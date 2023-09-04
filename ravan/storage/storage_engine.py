from sqlmodel import Session, SQLModel, create_engine

from ravan.helpers.singleton import SingletonMeta


class StorageEngine(metaclass=SingletonMeta):
    def __init__(self, db_uri=None) -> None:
        if db_uri:
            # TODO refactor this to use a config file
            sqlite_filename = "journal.ravan.sqlite"
            db_uri = f"sqlite:///{sqlite_filename}"
        self._engine = create_engine(db_uri)

    def init_storage(self):
        SQLModel.metadata.create_all(self._engine)

    def session(self):
        return Session(self._engine)
