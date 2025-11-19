from sqlalchemy import Column, Integer, Date, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from .base import Base


class ExamRecord(Base):
    """Модель для таблицы ExamRecord (Записи об экзаменах)"""
    __tablename__ = 'exam_record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ex_list_id = Column(Integer, ForeignKey('examination_list.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)
    grade = Column(Integer, nullable=False)
    is_appeal = Column(Boolean, default=False)
    exam_date = Column(Date, nullable=False)

    examination_list = relationship("ExaminationList", back_populates="exam_records")
    subject = relationship("Subject", back_populates="exam_records")