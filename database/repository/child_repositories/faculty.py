from sqlalchemy.orm import Session, class_mapper
from database.models import Faculty

class FacultyRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str):
        faculty = Faculty(faculty_name=name)  # Используем новое имя поля
        self.session.add(faculty)
        self.session.flush()

    def bulk_create(self, faculties_data):
        self.session.bulk_insert_mappings(class_mapper(Faculty), faculties_data)
        self.session.flush()

    def get_count(self):
        return self.session.query(Faculty).count()

    def get_sample(self, limit=None):
        query = self.session.query(Faculty.faculty_name)  # Используем новое имя поля
        return query.limit(limit).all() if limit else query.first()