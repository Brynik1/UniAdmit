from sqlalchemy.orm import Session, class_mapper
from datetime import date

from database.models import ExamSchedule, ExamType


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
        self.session.flush()

    def get_count(self):
        return self.session.query(ExamSchedule).count()