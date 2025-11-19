from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base


class Stream(Base):
    """Модель для таблицы Stream (Потоки)"""
    __tablename__ = 'stream'

    id = Column(Integer, primary_key=True, autoincrement=True)
    stream_name = Column(String, nullable=False)  # Изменено с name

    stream_groups = relationship("StreamGroup", back_populates="stream")
    exam_schedules = relationship("ExamSchedule", back_populates="stream")