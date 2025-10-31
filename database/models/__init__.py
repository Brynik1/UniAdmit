"""
Модели данных для системы управления абитуриентами
"""

from .models import (
    Base,
    Faculty,
    Department,
    School,
    Subject,
    StudyGroup,
    ExaminationList,
    Stream,
    Abiturient,
    ExamRecord,
    StreamGroup,
    ExamSchedule,
    MedalType,
    ExamType
)

__all__ = [
    'Base',
    'Faculty',
    'Department',
    'School',
    'Subject',
    'StudyGroup',
    'ExaminationList',
    'Stream',
    'Abiturient',
    'ExamRecord',
    'StreamGroup',
    'ExamSchedule',
    'MedalType',
    'ExamType'
]