from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.orm import relationship

from .base import Base


class StudyGroup(Base):
    """Модель для таблицы StudyGroup (Учебные группы)"""
    __tablename__ = 'study_group'

    id = Column(Integer, primary_key=True, autoincrement=True)
    group_name = Column(String, nullable=False)  # Изменено с name

    examination_lists = relationship("ExaminationList", back_populates="group")
    stream_groups = relationship("StreamGroup", back_populates="group")

    __table_args__ = (
        Index('ix_study_group_name', 'group_name'),
    )