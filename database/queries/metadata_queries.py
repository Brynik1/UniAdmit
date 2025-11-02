from database.models import (
    Faculty, Department, Abiturient, School,
    Subject, StudyGroup
)


def get_faculties_with_students(session):
    """Получает факультеты с абитуриентами"""
    return session.query(Faculty.name) \
        .join(Department, Faculty.id == Department.faculty_id) \
        .join(Abiturient, Department.id == Abiturient.department_id) \
        .distinct() \
        .all()


def get_students_sample(session):
    """Получает примеры студентов"""
    return session.query(
        Abiturient.last_name,
        Abiturient.first_name
    ).distinct().all()


def get_groups_sample(session):
    """Получает примеры групп"""
    return session.query(StudyGroup.name) \
        .distinct() \
        .all()


def get_subjects_sample(session):
    """Получает примеры предметов"""
    return session.query(Subject.name) \
        .distinct() \
        .all()


def get_schools(session, limit: int = None):
    """Получает все школы"""
    query = session.query(School)
    return query.order_by(School.id.desc()).limit(limit).all() if limit else query.all()




