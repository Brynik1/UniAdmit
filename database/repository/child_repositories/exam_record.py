from sqlalchemy.orm import Session, class_mapper
from datetime import date

from database.models import ExamRecord


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
        self.session.flush()

    def get_count(self):
        return self.session.query(ExamRecord).count()