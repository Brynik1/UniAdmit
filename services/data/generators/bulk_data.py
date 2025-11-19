from faker import Faker
import random

from database.models import MedalType, ExamType

fake = Faker('ru_RU')


def get_faculties(count):
    """Генерация факультетов и кафедр"""
    for i in range(count):
        faculty = {"faculty_name": f"Факультет №{i}"}
        yield faculty


def get_departments(faculty_count):
    for i in range(faculty_count):
        departments = [
            {"department_name": f"Кафедра A{i}", "faculty_id": i + 1},
            {"department_name": f"Кафедра B{i}", "faculty_id": i + 1}
        ]
        for department in departments:
            yield department


def get_schools(count):
    """Генерация школ"""
    for i in range(count):
        school = {"school_name": f"Школа №{i}", "address": "г. Санкт-Петербург"}
        yield school


def get_subjects(count):
    """Генерация предметов"""
    for i in range(count):
        subject = {"subject_name": f"Предмет №{i}"}
        yield subject


def get_study_groups(count):
    """Генерация учебных групп"""
    for i in range(count):
        group = {"group_name": f"Группа №{i}"}
        yield group


def get_streams(count):
    """Генерация потоков"""
    for i in range(count):
        stream = {"stream_name": f"Поток №{i}"}
        yield stream


def get_examination_lists(count, group_count):
    """Генерация экзаменационных ведомостей"""
    for i in range(count):
        exam_list = {"group_id": (i % group_count) + 1}
        yield exam_list


def get_abiturients(count, department_count, school_count):
    """Генерация абитуриентов (строго один к одному с ведомостями)"""
    for i in range(count):
        gender = random.choice(['male', 'female'])
        last_name = fake.last_name_male() if gender == 'male' else fake.last_name_female()
        first_name = fake.first_name_male() if gender == 'male' else fake.first_name_female()
        patronymic = fake.middle_name_male() if gender == 'male' else fake.middle_name_female()

        abiturient = {
            "last_name": last_name,
            "first_name": first_name,
            "patronymic": patronymic,
            "passport_series": str(i % 10000).zfill(4),
            "passport_number": str(i % 1000000).zfill(6),
            "passport_issued_by": "Министерство Внутренних Дел",
            "graduation_year": 2025,
            "has_medal": MedalType.NONE,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": True,
            "department_id": (i % department_count) + 1,
            "school_id": (i % school_count) + 1,
            "ex_list_id": i + 1  # ID соответствует ID ведомости (строго один к одному)
        }
        yield abiturient


def get_exam_records(total_exam_lists, subject_count):
    """Генерация записей об экзаменах"""
    for exam_list_id in range(1, total_exam_lists + 1):
        subject_ids = random.sample(range(1, subject_count + 1), 3)

        for subject_id in subject_ids:
            exam_record = {
                "ex_list_id": exam_list_id,
                "subject_id": subject_id,
                "grade": (exam_list_id + subject_id) % 100 + 1,
                "is_appeal": False,
                "exam_date": fake.date_between(start_date='-1y', end_date='today')
            }
            yield exam_record


def get_stream_groups(group_count, stream_count):
    """Генерация связей потоков и групп"""
    for group_id in range(1, group_count + 1):
        stream_ids = random.sample(range(1, stream_count + 1), 2)

        for stream_id in stream_ids:
            stream_group = {
                "group_id": group_id,
                "stream_id": stream_id
            }
            yield stream_group


def get_exam_schedules(stream_count, subject_count):
    """Генерация расписания экзаменов"""
    for stream_id in range(1, stream_count + 1):
        subject_ids = random.sample(range(1, subject_count + 1), 3)

        for subject_id in subject_ids:
            exam_date = fake.date_between(start_date='-1y', end_date='+30d')
            classroom = str(fake.random_int(100, 500))

            exam_schedule = {
                "stream_id": stream_id,
                "subject_id": subject_id,
                "classroom": classroom,
                "exam_type": ExamType.EXAM,
                "schedule_date": exam_date
            }
            yield exam_schedule


def generate_bulk_data(
        abiturient_count=10000,
        faculty_count=10000,
        school_count=10000,
        group_count=10000,
        stream_count=20000,
        subject_count=10000,
        batch_size=100
):
    """
    Основная функция для генерации большого количества тестовых данных
    Возвращает батчи данных
    """
    batch = []

    for data in get_faculties(faculty_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "faculty", batch
            batch = []

    if batch:
        yield "faculty", batch
        batch = []

    for data in get_departments(faculty_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "department", batch
            batch = []

    if batch:
        yield "department", batch
        batch = []

    for data in get_schools(school_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "school", batch
            batch = []

    if batch:
        yield "school", batch
        batch = []

    for data in get_subjects(subject_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "subject", batch
            batch = []

    if batch:
        yield "subject", batch
        batch = []

    for data in get_study_groups(group_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "study_group", batch
            batch = []

    if batch:
        yield "study_group", batch
        batch = []

    for data in get_streams(stream_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "stream", batch
            batch = []

    if batch:
        yield "stream", batch
        batch = []

    department_count = faculty_count * 2
    for data in get_examination_lists(abiturient_count, group_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "examination_list", batch
            batch = []

    if batch:
        yield "examination_list", batch
        batch = []

    for data in get_abiturients(abiturient_count, department_count, school_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "abiturient", batch
            batch = []

    if batch:
        yield "abiturient", batch
        batch = []

    for data in get_exam_records(abiturient_count, subject_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "exam_record", batch
            batch = []

    if batch:
        yield "exam_record", batch
        batch = []

    for data in get_stream_groups(group_count, stream_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "stream_group", batch
            batch = []

    if batch:
        yield "stream_group", batch
        batch = []

    for data in get_exam_schedules(stream_count, subject_count):
        batch.append(data)
        if len(batch) >= batch_size:
            yield "exam_schedule", batch
            batch = []

    if batch:
        yield "exam_schedule", batch