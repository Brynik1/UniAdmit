from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from .base import Base


class School(Base):
    """Модель для таблицы School (Школы)"""
    __tablename__ = 'school'

    id = Column(Integer, primary_key=True, autoincrement=True)
    school_name = Column(String, nullable=False)  # Изменено с name
    address = Column(Text, nullable=False)

    abiturients = relationship("Abiturient", back_populates="school")