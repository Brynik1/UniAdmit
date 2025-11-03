from sqlalchemy.orm import Session
from fastapi import Depends

from database import db_manager, MainRepository


def get_main_repository(db: Session = Depends(db_manager.get_db)) -> MainRepository:
    return MainRepository(db)