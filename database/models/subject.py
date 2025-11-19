from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Subject(Base):
    """Модель для таблицы Subject (Предметы)"""
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True, autoincrement=True)
    subject_name = Column(String, nullable=False)  # Изменено с name

    exam_records = relationship("ExamRecord", back_populates="subject")
    exam_schedules = relationship("ExamSchedule", back_populates="subject")