from contextlib import contextmanager
from database import db_manager, MainRepository


@contextmanager
def get_main_repository():
    """
    Контекстный менеджер для получения репозитория
    """
    with db_manager.get_session() as session:
        repo = MainRepository(session)
        yield repo

