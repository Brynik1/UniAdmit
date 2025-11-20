import enum
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Enum, Boolean, Index
from sqlalchemy.orm import relationship

from .base import Base


class MedalType(enum.Enum):
    GOLD = "GOLD"
    SILVER = "SILVER"
    NONE = "NONE"


class Abiturient(Base):
    """Модель для таблицы Abiturient (Абитуриенты)"""
    __tablename__ = 'abiturient'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    patronymic = Column(String)
    passport_series = Column(String, nullable=False)
    passport_number = Column(String, nullable=False)
    passport_issued_by = Column(Text, nullable=False)
    graduation_year = Column(Integer, nullable=False)
    has_medal = Column(Enum(MedalType), nullable=False)
    documents_submitted = Column(Boolean, default=False)
    documents_withdrawn = Column(Boolean, default=False)
    is_enrolled = Column(Boolean, default=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)
    ex_list_id = Column(Integer, ForeignKey('examination_list.id'), nullable=False)

    department = relationship("Department", back_populates="abiturients")
    school = relationship("School", back_populates="abiturients")
    examination_list = relationship("ExaminationList", back_populates="abiturients")

    __table_args__ = (
        Index('ix_abiturient_names', 'last_name', 'first_name'),
        Index('ix_abiturient_department', 'department_id'),
    )