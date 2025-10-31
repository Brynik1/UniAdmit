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


def get_faculties_count(session):
    """Получает количество факультетов"""
    return session.query(Faculty).count()


def get_students_count(session):
    """Получает количество абитуриентов"""
    return session.query(Abiturient).count()


def get_groups_count(session):
    """Получает количество групп"""
    return session.query(StudyGroup).count()


def get_subjects_count(session):
    """Получает количество предметов"""
    return session.query(Subject).count()


def get_schools(
        session,
        limit: int = None
):
    """Получает все школы"""
    query = session.query(School)
    return query.limit(limit).all() if limit else query.all()


def create_school(
        name: str,
        address: str,
        session
):
    """Создает новую школу"""
    school = School(name=name, address=address)
    session.add(school)
    session.commit()


def update_school(
        session,
        name: str,
        address: str,
        new_name: str = None,
        new_address: str = None,
):
    """Обновляет данные школы"""
    school = session.query(School).filter(
        School.name == name,
        School.address == address
    ).first()

    if school:
        if new_name is not None:
            school.name = new_name
        if new_address is not None:
            school.address = new_address

        session.commit()
        return True

    return False


def delete_school(
        session,
        name: str,
        address: str
):
    """Удаляет школу"""
    school = session.query(School).filter(
        School.name == name,
        School.address == address
    ).first()

    if school:
        session.delete(school)
        session.commit()
        return True

    return False

