from sqlalchemy.orm import Session, class_mapper

from database.models import StudyGroup


class StudyGroupRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str):
        group = StudyGroup(name=name)
        self.session.add(group)
        self.session.flush()

    def bulk_create(self, groups_data):
        self.session.bulk_insert_mappings(class_mapper(StudyGroup), groups_data)
        self.session.flush()

    def get_count(self):
        return self.session.query(StudyGroup).count()

    def get_sample(self, limit=None):
        query = self.session.query(StudyGroup.name)
        return query.limit(limit).all() if limit else query.first()