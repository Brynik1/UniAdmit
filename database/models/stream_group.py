from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class StreamGroup(Base):
    """Модель для таблицы StreamGroup (Связь потоков и групп)"""
    __tablename__ = 'stream_group'

    group_id = Column(Integer, ForeignKey('study_group.id'), primary_key=True)
    stream_id = Column(Integer, ForeignKey('stream.id'), primary_key=True)

    group = relationship("StudyGroup", back_populates="stream_groups")
    stream = relationship("Stream", back_populates="stream_groups")