from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from core.config import config

from database.models import Base


class DatabaseManager:
    def __init__(self, database_url):
        self.database_url = database_url
        self.engine = create_engine(self.database_url)
        self.SessionLocal = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self.engine
        )

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)

    def drop_tables(self):
        Base.metadata.drop_all(bind=self.engine)

    def check_tables(self):
        """
        Простая проверка, что все модели созданы в БД и нет лишних таблиц.
        """
        inspector = inspect(self.engine)
        db_tables = set(inspector.get_table_names())
        model_tables = set(Base.metadata.tables.keys())

        return db_tables == model_tables

    @contextmanager
    def get_session(self):
        """
        Контекстный менеджер для сессии (для сервисов, бенчмарков)
        """
        session = self.SessionLocal()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()

    def get_db(self):
        """
        Генератор для FastAPI
        """
        session = self.SessionLocal()
        try:
            yield session
        finally:
            session.close()


# Глобальный экземпляр менеджера БД
db_manager = DatabaseManager(config.database.connection_string)