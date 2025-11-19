from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class ExaminationList(Base):
    """Модель для таблицы ExaminationList (Экзаменационные ведомости)"""
    __tablename__ = 'examination_list'

    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey('study_group.id'), nullable=False)

    group = relationship("StudyGroup", back_populates="examination_lists")
    abiturients = relationship("Abiturient", back_populates="examination_list")
    exam_records = relationship("ExamRecord", back_populates="examination_list")