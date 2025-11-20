from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.orm import relationship

from .base import Base


class Faculty(Base):
    """Модель для таблицы Faculty (Факультеты)"""
    __tablename__ = 'faculty'

    id = Column(Integer, primary_key=True, autoincrement=True)
    faculty_name = Column(String, nullable=False)  # Изменено с name

    departments = relationship("Department", back_populates="faculty")

    __table_args__ = (
        Index('ix_faculty_name', 'faculty_name'),
    )