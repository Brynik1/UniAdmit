from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Enum, Boolean
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
import enum


class MedalType(enum.Enum):
    GOLD = "GOLD"
    SILVER = "SILVER"
    NONE = "NONE"


class ExamType(enum.Enum):
    CONSULTATION = "CONSULTATION"
    EXAM = "EXAM"


# Базовый класс для всех моделей
Base = declarative_base()


class Faculty(Base):
    """Модель для таблицы Faculty (Факультеты)"""
    __tablename__ = 'faculty'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    departments = relationship("Department", back_populates="faculty")


class Department(Base):
    """Модель для таблицы Department (Кафедры)"""
    __tablename__ = 'department'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    faculty_id = Column(Integer, ForeignKey('faculty.id'), nullable=False)

    faculty = relationship("Faculty", back_populates="departments")
    abiturients = relationship("Abiturient", back_populates="department")


class School(Base):
    """Модель для таблицы School (Школы)"""
    __tablename__ = 'school'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(Text, nullable=False)

    abiturients = relationship("Abiturient", back_populates="school")


class Subject(Base):
    """Модель для таблицы Subject (Предметы)"""
    __tablename__ = 'subject'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    exam_records = relationship("ExamRecord", back_populates="subject")
    exam_schedules = relationship("ExamSchedule", back_populates="subject")


class StudyGroup(Base):
    """Модель для таблицы StudyGroup (Учебные группы)"""
    __tablename__ = 'study_group'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    examination_lists = relationship("ExaminationList", back_populates="group")
    stream_groups = relationship("StreamGroup", back_populates="group")


class ExaminationList(Base):
    """Модель для таблицы ExaminationList (Экзаменационные ведомости)"""
    __tablename__ = 'examination_list'

    id = Column(Integer, primary_key=True, autoincrement=True)
    group_id = Column(Integer, ForeignKey('study_group.id'), nullable=False)

    group = relationship("StudyGroup", back_populates="examination_lists")
    abiturients = relationship("Abiturient", back_populates="examination_list")
    exam_records = relationship("ExamRecord", back_populates="examination_list")


class Stream(Base):
    """Модель для таблицы Stream (Потоки)"""
    __tablename__ = 'stream'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

    stream_groups = relationship("StreamGroup", back_populates="stream")
    exam_schedules = relationship("ExamSchedule", back_populates="stream")


class Abiturient(Base):
    """Модель для таблицы Abiturient (Абитуриенты)"""
    __tablename__ = 'abiturient'

    id = Column(Integer, primary_key=True, autoincrement=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    patronymic = Column(String)  # Может быть NULL
    passport_series = Column(String, nullable=False)
    passport_number = Column(String, nullable=False)
    passport_issued_by = Column(Text, nullable=False)
    graduation_year = Column(Integer, nullable=False)
    has_medal = Column(Enum(MedalType), nullable=False)  # Используем Enum
    documents_submitted = Column(Boolean, default=False)
    documents_withdrawn = Column(Boolean, default=False)
    is_enrolled = Column(Boolean, default=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    school_id = Column(Integer, ForeignKey('school.id'), nullable=False)
    ex_list_id = Column(Integer, ForeignKey('examination_list.id'), nullable=False)

    department = relationship("Department", back_populates="abiturients")
    school = relationship("School", back_populates="abiturients")
    examination_list = relationship("ExaminationList", back_populates="abiturients")


class ExamRecord(Base):
    """Модель для таблицы ExamRecord (Записи об экзаменах)"""
    __tablename__ = 'exam_record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ex_list_id = Column(Integer, ForeignKey('examination_list.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)
    grade = Column(Integer, nullable=False)
    is_appeal = Column(Boolean, default=False)
    record_date = Column(Date, nullable=False)

    examination_list = relationship("ExaminationList", back_populates="exam_records")
    subject = relationship("Subject", back_populates="exam_records")


class StreamGroup(Base):
    """Модель для таблицы StreamGroup (Связь потоков и групп)"""
    __tablename__ = 'stream_group'

    group_id = Column(Integer, ForeignKey('study_group.id'), primary_key=True)
    stream_id = Column(Integer, ForeignKey('stream.id'), primary_key=True)

    group = relationship("StudyGroup", back_populates="stream_groups")
    stream = relationship("Stream", back_populates="stream_groups")


class ExamSchedule(Base):
    """Модель для таблицы ExamSchedule (Расписание экзаменов)"""
    __tablename__ = 'exam_schedule'

    id = Column(Integer, primary_key=True, autoincrement=True)
    stream_id = Column(Integer, ForeignKey('stream.id'), nullable=False)
    subject_id = Column(Integer, ForeignKey('subject.id'), nullable=False)
    classroom = Column(String, nullable=False)
    exam_type = Column(Enum(ExamType), nullable=False)
    record_date = Column(Date, nullable=False)

    stream = relationship("Stream", back_populates="exam_schedules")
    subject = relationship("Subject", back_populates="exam_schedules")
