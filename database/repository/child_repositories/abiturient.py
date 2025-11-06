from sqlalchemy.orm import Session, class_mapper

from database.models import Abiturient, MedalType


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
        self.session.flush()

    def get_count(self):
        return self.session.query(Abiturient).count()

    def get_sample(self, limit=None):
        query = self.session.query(
            Abiturient.last_name,
            Abiturient.first_name
        )
        return query.limit(limit).all() if limit else query.first()