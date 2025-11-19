from sqlalchemy.orm import Session, class_mapper

from database.models import Subject


class SubjectRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str):
        subject = Subject(subject_name=name)
        self.session.add(subject)
        self.session.flush()

    def bulk_create(self, subjects_data):
        self.session.bulk_insert_mappings(class_mapper(Subject), subjects_data)
        self.session.flush()

    def get_count(self):
        return self.session.query(Subject).count()

    def get_sample(self, limit=None):
        query = self.session.query(Subject.subject_name)
        return query.limit(limit).all() if limit else query.first()