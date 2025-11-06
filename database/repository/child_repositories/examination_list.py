from sqlalchemy.orm import Session, class_mapper

from database.models import ExaminationList


class ExaminationListRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, group_id: int):
        exam_list = ExaminationList(group_id=group_id)
        self.session.add(exam_list)
        self.session.flush()

    def bulk_create(self, exam_lists_data):
        self.session.bulk_insert_mappings(class_mapper(ExaminationList), exam_lists_data)
        self.session.flush()