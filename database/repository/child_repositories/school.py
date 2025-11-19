from sqlalchemy.orm import Session, class_mapper

from database.models import School

class SchoolRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, address: str):
        school = School(school_name=name, address=address)
        self.session.add(school)
        self.session.flush()

    def bulk_create(self, schools_data):
        self.session.bulk_insert_mappings(class_mapper(School), schools_data)
        self.session.flush()

    def update(self, name: str, address: str, new_name: str = None, new_address: str = None):
        school = self.session.query(School).filter(
            School.school_name == name,
            School.address == address
        ).first()

        if school:
            if new_name is not None:
                school.name = new_name
            if new_address is not None:
                school.address = new_address

            self.session.flush()
            return True

        return False

    def delete(self, name: str, address: str):
        school = self.session.query(School).filter(
            School.school_name == name,
            School.address == address
        ).first()

        if school:
            self.session.delete(school)
            self.session.commit()
            return True

        return False

    def get_count(self):
        return self.session.query(School).count()

    def get_sample(self, limit=None):
        query = self.session.query(School.school_name, School.address)
        return query.order_by(School.id.desc()).limit(limit).all() if limit else query.first()