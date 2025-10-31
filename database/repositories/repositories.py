from sqlalchemy.orm import Session, class_mapper
from datetime import date

from database.models import (
    Faculty, Department, School, Subject, StudyGroup,
    ExaminationList, Stream, Abiturient, ExamRecord,
    StreamGroup, ExamSchedule, MedalType, ExamType
)


class FacultyRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str):
        faculty = Faculty(name=name)
        self.session.add(faculty)
        self.session.flush()

    def bulk_create(self, faculties_data):
        self.session.bulk_insert_mappings(class_mapper(Faculty), faculties_data)


class DepartmentRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, faculty_id: int):
        department = Department(name=name, faculty_id=faculty_id)
        self.session.add(department)
        self.session.flush()

    def bulk_create(self, departments_data):
        self.session.bulk_insert_mappings(class_mapper(Department), departments_data)


class SchoolRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, address: str):
        school = School(name=name, address=address)
        self.session.add(school)
        self.session.flush()

    def bulk_create(self, schools_data):
        self.session.bulk_insert_mappings(class_mapper(School), schools_data)


class SubjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str):
        subject = Subject(name=name)
        self.session.add(subject)
        self.session.flush()

    def bulk_create(self, subjects_data):
        self.session.bulk_insert_mappings(class_mapper(Subject), subjects_data)


class StudyGroupRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str):
        group = StudyGroup(name=name)
        self.session.add(group)
        self.session.flush()

    def bulk_create(self, groups_data):
        self.session.bulk_insert_mappings(class_mapper(StudyGroup), groups_data)


class ExaminationListRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, group_id: int):
        exam_list = ExaminationList(group_id=group_id)
        self.session.add(exam_list)
        self.session.flush()

    def bulk_create(self, exam_lists_data):
        self.session.bulk_insert_mappings(class_mapper(ExaminationList), exam_lists_data)


class StreamRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str):
        stream = Stream(name=name)
        self.session.add(stream)
        self.session.flush()

    def bulk_create(self, streams_data):
        self.session.bulk_insert_mappings(class_mapper(Stream), streams_data)


class AbiturientRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(
            self,
            last_name: str,
            first_name: str,
            passport_series: str,
            passport_number: str,
            passport_issued_by: str,
            graduation_year: int,
            has_medal: MedalType,
            department_id: int,
            school_id: int,
            ex_list_id: int,
            patronymic: str = None,
            documents_submitted: bool = False,
            documents_withdrawn: bool = False,
            is_enrolled: bool = False
    ):
        abiturient = Abiturient(
            last_name=last_name,
            first_name=first_name,
            patronymic=patronymic,
            passport_series=passport_series,
            passport_number=passport_number,
            passport_issued_by=passport_issued_by,
            graduation_year=graduation_year,
            has_medal=has_medal,
            documents_submitted=documents_submitted,
            documents_withdrawn=documents_withdrawn,
            is_enrolled=is_enrolled,
            department_id=department_id,
            school_id=school_id,
            ex_list_id=ex_list_id
        )
        self.session.add(abiturient)
        self.session.flush()

    def bulk_create(self, abiturients_data):
        self.session.bulk_insert_mappings(class_mapper(Abiturient), abiturients_data)


class ExamRecordRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(
            self,
            ex_list_id: int,
            subject_id: int,
            grade: int,
            record_date: date,
            is_appeal: bool = False
    ):
        exam_record = ExamRecord(
            ex_list_id=ex_list_id,
            subject_id=subject_id,
            grade=grade,
            is_appeal=is_appeal,
            record_date=record_date
        )
        self.session.add(exam_record)
        self.session.flush()

    def bulk_create(self, exam_records_data):
        self.session.bulk_insert_mappings(class_mapper(ExamRecord), exam_records_data)


class StreamGroupRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, group_id: int, stream_id: int):
        stream_group = StreamGroup(group_id=group_id, stream_id=stream_id)
        self.session.add(stream_group)
        self.session.flush()

    def bulk_create(self, stream_groups_data):
        self.session.bulk_insert_mappings(class_mapper(StreamGroup), stream_groups_data)


class ExamScheduleRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(
            self,
            stream_id: int,
            subject_id: int,
            classroom: str,
            exam_type: ExamType,
            record_date: date
    ):
        exam_schedule = ExamSchedule(
            stream_id=stream_id,
            subject_id=subject_id,
            classroom=classroom,
            exam_type=exam_type,
            record_date=record_date
        )
        self.session.add(exam_schedule)
        self.session.flush()

    def bulk_create(self, exam_schedules_data):
        self.session.bulk_insert_mappings(class_mapper(ExamSchedule), exam_schedules_data)