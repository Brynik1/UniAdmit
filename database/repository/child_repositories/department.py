from sqlalchemy.orm import Session, class_mapper

from database.models import Department



class DepartmentRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, faculty_id: int):
        department = Department(name=name, faculty_id=faculty_id)
        self.session.add(department)
        self.session.flush()

    def bulk_create(self, departments_data):
        self.session.bulk_insert_mappings(class_mapper(Department), departments_data)
        self.session.flush()

    def get_count(self):
        return self.session.query(Department).count()