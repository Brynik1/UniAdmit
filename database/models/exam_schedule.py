import enum
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum, Index
from sqlalchemy.orm import relationship

from .base import Base


class ExamType(enum.Enum):
    CONSULTATION = "CONSULTATION"
    EXAM = "EXAM"


class ExamSchedule(Base):
    """Модель для таблицы ExamSchedule (Расписание экзаменов)"""
    __tablename__ = 'exam_schedule'

    id = Column(Integer, primary_key=True, autoincrement=True)
    stream_id = Column(Integer, ForeignKey('stream.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)
    classroom = Column(String, nullable=False)
    exam_type = Column(Enum(ExamType), nullable=False)
    schedule_date = Column(Date, nullable=False)

    stream = relationship("Stream", back_populates="exam_schedules")
    subject = relationship("Subject", back_populates="exam_schedules")

    __table_args__ = (
        Index('ix_exam_schedule_stream', 'stream_id'),
        Index('ix_exam_schedule_subject', 'subject_id'),
    )