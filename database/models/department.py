from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .base import Base


class Department(Base):
    """Модель для таблицы Department (Кафедры)"""
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    department_name = Column(String, nullable=False)  # Изменено с name
    faculty_id = Column(Integer, ForeignKey('faculty.id'), nullable=False)

    faculty = relationship("Faculty", back_populates="departments")
    abiturients = relationship("Abiturient", back_populates="department")