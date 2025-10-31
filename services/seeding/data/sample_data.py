from datetime import date
from database.models import MedalType, ExamType


def generate_sample_data():
    """
    Генерирует небольшой набор тестовых данных
    """

    faculties = [
        {"name": "Факультет компьютерных технологий"},
        {"name": "Факультет экономики"},
        {"name": "Факультет юриспруденции"},
        {"name": "Факультет филологии"},
        {"name": "Факультет математики"},
        {"name": "Факультет физики"},
        {"name": "Факультет химии"},
        {"name": "Факультет биологии"},
        {"name": "Факультет истории"},
        {"name": "Факультет психологии"}
    ]
    yield "faculty", faculties

    departments = [
        {"name": "Кафедра программирования", "faculty_id": 1},
        {"name": "Кафедра искусственного интеллекта", "faculty_id": 1},
        {"name": "Кафедра экономической теории", "faculty_id": 2},
        {"name": "Кафедра банковского дела", "faculty_id": 2},
        {"name": "Кафедра гражданского права", "faculty_id": 3},
        {"name": "Кафедра уголовного права", "faculty_id": 3},
        {"name": "Кафедра русской литературы", "faculty_id": 4},
        {"name": "Кафедра иностранных языков", "faculty_id": 4},
        {"name": "Кафедра высшей математики", "faculty_id": 5},
        {"name": "Кафедра прикладной математики", "faculty_id": 5}
    ]
    yield "department", departments

    schools = [
        {"name": "Лицей №1535", "address": "г. Санкт-Петербург, ул. Ушинского, д. 52"},
        {"name": "Гимназия №1567", "address": "г. Санкт-Петербург, ул. Пр. Попова, д. 11"},
        {"name": "Школа №179", "address": "г. Санкт-Петербург, ул. Большая Пушкарская, д. 5/6"},
        {"name": "Вторая школа", "address": "г. Санкт-Петербург, ул. Фотиевой, д. 18"},
        {"name": "Гимназия №1514", "address": "г. Санкт-Петербург, ул. Крупской, д. 12"},
        {"name": "Школа №57", "address": "г. Санкт-Петербург, Малый проспект П.С., д. 7/10"},
        {"name": "Лицей №1580", "address": "г. Санкт-Петербург, Балтийский проспект, д. 6А"},
        {"name": "Гимназия №1543", "address": "г. Санкт-Петербург, ул. Бакинского, д. 3"},
        {"name": "Школа №2007", "address": "г. Санкт-Петербург, ул. Горчакова, д. 9, к. 1"},
        {"name": "Лицей №1501", "address": "г. Санкт-Петербург, Тихвинский пер., д. 3"}
    ]
    yield "school", schools

    subjects = [
        {"name": "Математика"},
        {"name": "Русский язык"},
        {"name": "Физика"},
        {"name": "Информатика"},
        {"name": "История"},
        {"name": "Обществознание"},
        {"name": "Литература"},
        {"name": "Английский язык"},
        {"name": "Химия"},
        {"name": "Биология"}
    ]
    yield "subject", subjects

    groups = [
        {"name": "ПИ-101"},
        {"name": "ПИ-102"},
        {"name": "ЭК-101"},
        {"name": "ЭК-102"},
        {"name": "ЮР-101"},
        {"name": "ЮР-102"},
        {"name": "ФЛ-101"},
        {"name": "ФЛ-102"},
        {"name": "МАТ-101"},
        {"name": "МАТ-102"}
    ]
    yield "study_group", groups

    streams = [
        {"name": "Технический поток 1"},
        {"name": "Экономический поток"},
        {"name": "Юридический поток"},
        {"name": "Филологический поток"},
        {"name": "Математический поток"},
        {"name": "Гуманитарный поток 1"},
        {"name": "Гуманитарный поток 2"},
        {"name": "Технический поток 3"},
        {"name": "Естественнонаучный поток"},
        {"name": "Общий поток"}
    ]
    yield "stream", streams

    examination_lists = [
        {"group_id": 1},
        {"group_id": 1},
        {"group_id": 2},
        {"group_id": 2},
        {"group_id": 3},
        {"group_id": 3},
        {"group_id": 4},
        {"group_id": 4},
        {"group_id": 5},
        {"group_id": 5}
    ]
    yield "examination_list", examination_lists

    abiturients = [
        {
            "last_name": "Иванов",
            "first_name": "Алексей",
            "patronymic": "Петрович",
            "passport_series": "4510",
            "passport_number": "123456",
            "passport_issued_by": "ОУФМС России по г. Москве",
            "graduation_year": 2023,
            "has_medal": MedalType.GOLD.value,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": True,
            "department_id": 1,
            "school_id": 1,
            "ex_list_id": 1
        },
        {
            "last_name": "Петрова",
            "first_name": "Мария",
            "patronymic": "Сергеевна",
            "passport_series": "4511",
            "passport_number": "123457",
            "passport_issued_by": "ОУФМС России по г. Москве",
            "graduation_year": 2023,
            "has_medal": MedalType.SILVER.value,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": True,
            "department_id": 1,
            "school_id": 2,
            "ex_list_id": 2
        },
        {
            "last_name": "Сидоров",
            "first_name": "Дмитрий",
            "patronymic": "Иванович",
            "passport_series": "4512",
            "passport_number": "123458",
            "passport_issued_by": "ОУФМС России по г. Москве",
            "graduation_year": 2023,
            "has_medal": MedalType.NONE.value,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": True,
            "department_id": 2,
            "school_id": 3,
            "ex_list_id": 3
        },
        {
            "last_name": "Кузнецова",
            "first_name": "Анна",
            "patronymic": "Владимировна",
            "passport_series": "4513",
            "passport_number": "123459",
            "passport_issued_by": "ОУФМС России по г. Москве",
            "graduation_year": 2023,
            "has_medal": MedalType.GOLD.value,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": True,
            "department_id": 3,
            "school_id": 4,
            "ex_list_id": 4
        },
        {
            "last_name": "Попов",
            "first_name": "Сергей",
            "patronymic": "Александрович",
            "passport_series": "4514",
            "passport_number": "123460",
            "passport_issued_by": "ОУФМС России по г. Москве",
            "graduation_year": 2023,
            "has_medal": MedalType.NONE.value,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": False,
            "department_id": 4,
            "school_id": 5,
            "ex_list_id": 5
        },
        {
            "last_name": "Васильева",
            "first_name": "Елена",
            "patronymic": "Дмитриевна",
            "passport_series": "4515",
            "passport_number": "123461",
            "passport_issued_by": "ОУФМС России по г. Москве",
            "graduation_year": 2023,
            "has_medal": MedalType.SILVER.value,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": True,
            "department_id": 5,
            "school_id": 6,
            "ex_list_id": 6
        },
        {
            "last_name": "Морозов",
            "first_name": "Иван",
            "patronymic": "Петрович",
            "passport_series": "4516",
            "passport_number": "123462",
            "passport_issued_by": "ОУФМС России по г. Москве",
            "graduation_year": 2023,
            "has_medal": MedalType.NONE.value,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": True,
            "department_id": 6,
            "school_id": 7,
            "ex_list_id": 7
        },
        {
            "last_name": "Новикова",
            "first_name": "Ольга",
            "patronymic": "Сергеевна",
            "passport_series": "4517",
            "passport_number": "123463",
            "passport_issued_by": "ОУФМС России по г. Москве",
            "graduation_year": 2023,
            "has_medal": MedalType.GOLD.value,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": True,
            "department_id": 7,
            "school_id": 8,
            "ex_list_id": 8
        },
        {
            "last_name": "Федоров",
            "first_name": "Павел",
            "patronymic": "Андреевич",
            "passport_series": "4518",
            "passport_number": "123464",
            "passport_issued_by": "ОУФМС России по г. Москве",
            "graduation_year": 2023,
            "has_medal": MedalType.NONE.value,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": False,
            "department_id": 8,
            "school_id": 9,
            "ex_list_id": 9
        },
        {
            "last_name": "Соколова",
            "first_name": "Татьяна",
            "patronymic": "Викторовна",
            "passport_series": "4519",
            "passport_number": "123465",
            "passport_issued_by": "ОУФМС России по г. Москве",
            "graduation_year": 2023,
            "has_medal": MedalType.SILVER.value,
            "documents_submitted": True,
            "documents_withdrawn": False,
            "is_enrolled": True,
            "department_id": 9,
            "school_id": 10,
            "ex_list_id": 10
        }
    ]
    yield "abiturient", abiturients

    exam_records = [
        # Абитуриент 1
        {
            "ex_list_id": 1,
            "subject_id": 1,
            "grade": 95,
            "is_appeal": False,
            "record_date": date(2023, 6, 15)
        },
        {
            "ex_list_id": 1,
            "subject_id": 2,
            "grade": 88,
            "is_appeal": False,
            "record_date": date(2023, 6, 20)
        },
        {
            "ex_list_id": 1,
            "subject_id": 4,
            "grade": 92,
            "is_appeal": False,
            "record_date": date(2023, 6, 25)
        },
        {
            "ex_list_id": 1,
            "subject_id": 3,
            "grade": 85,
            "is_appeal": True,
            "record_date": date(2023, 7, 1)
        },

        # Абитуриент 2
        {
            "ex_list_id": 2,
            "subject_id": 1,
            "grade": 87,
            "is_appeal": False,
            "record_date": date(2023, 6, 15)
        },
        {
            "ex_list_id": 2,
            "subject_id": 2,
            "grade": 91,
            "is_appeal": False,
            "record_date": date(2023, 6, 20)
        },
        {
            "ex_list_id": 2,
            "subject_id": 4,
            "grade": 89,
            "is_appeal": False,
            "record_date": date(2023, 6, 25)
        },
        {
            "ex_list_id": 2,
            "subject_id": 3,
            "grade": 82,
            "is_appeal": False,
            "record_date": date(2023, 6, 28)
        },

        # Абитуриент 3
        {
            "ex_list_id": 3,
            "subject_id": 1,
            "grade": 78,
            "is_appeal": False,
            "record_date": date(2023, 6, 15)
        },
        {
            "ex_list_id": 3,
            "subject_id": 2,
            "grade": 85,
            "is_appeal": False,
            "record_date": date(2023, 6, 20)
        },
        {
            "ex_list_id": 3,
            "subject_id": 4,
            "grade": 91,
            "is_appeal": False,
            "record_date": date(2023, 6, 25)
        },
        {
            "ex_list_id": 3,
            "subject_id": 3,
            "grade": 79,
            "is_appeal": True,
            "record_date": date(2023, 7, 2)
        },

        # Абитуриент 4
        {
            "ex_list_id": 4,
            "subject_id": 1,
            "grade": 94,
            "is_appeal": False,
            "record_date": date(2023, 6, 15)
        },
        {
            "ex_list_id": 4,
            "subject_id": 2,
            "grade": 90,
            "is_appeal": False,
            "record_date": date(2023, 6, 20)
        },
        {
            "ex_list_id": 4,
            "subject_id": 6,
            "grade": 87,
            "is_appeal": False,
            "record_date": date(2023, 6, 25)
        },
        {
            "ex_list_id": 4,
            "subject_id": 8,
            "grade": 92,
            "is_appeal": False,
            "record_date": date(2023, 6, 28)
        },

        # Абитуриент 5
        {
            "ex_list_id": 5,
            "subject_id": 1,
            "grade": 76,
            "is_appeal": False,
            "record_date": date(2023, 6, 15)
        },
        {
            "ex_list_id": 5,
            "subject_id": 2,
            "grade": 81,
            "is_appeal": False,
            "record_date": date(2023, 6, 20)
        },
        {
            "ex_list_id": 5,
            "subject_id": 6,
            "grade": 79,
            "is_appeal": False,
            "record_date": date(2023, 6, 25)
        },
        {
            "ex_list_id": 5,
            "subject_id": 8,
            "grade": 84,
            "is_appeal": False,
            "record_date": date(2023, 6, 28)
        },

        # Абитуриент 6
        {
            "ex_list_id": 6,
            "subject_id": 2,
            "grade": 89,
            "is_appeal": False,
            "record_date": date(2023, 6, 20)
        },
        {
            "ex_list_id": 6,
            "subject_id": 5,
            "grade": 85,
            "is_appeal": False,
            "record_date": date(2023, 6, 25)
        },
        {
            "ex_list_id": 6,
            "subject_id": 6,
            "grade": 91,
            "is_appeal": False,
            "record_date": date(2023, 6, 28)
        },
        {
            "ex_list_id": 6,
            "subject_id": 8,
            "grade": 87,
            "is_appeal": False,
            "record_date": date(2023, 7, 1)
        },

        # Абитуриент 7
        {
            "ex_list_id": 7,
            "subject_id": 2,
            "grade": 83,
            "is_appeal": False,
            "record_date": date(2023, 6, 20)
        },
        {
            "ex_list_id": 7,
            "subject_id": 5,
            "grade": 88,
            "is_appeal": False,
            "record_date": date(2023, 6, 25)
        },
        {
            "ex_list_id": 7,
            "subject_id": 6,
            "grade": 85,
            "is_appeal": False,
            "record_date": date(2023, 6, 28)
        },
        {
            "ex_list_id": 7,
            "subject_id": 8,
            "grade": 90,
            "is_appeal": False,
            "record_date": date(2023, 7, 1)
        },

        # Абитуриент 8
        {
            "ex_list_id": 8,
            "subject_id": 2,
            "grade": 93,
            "is_appeal": False,
            "record_date": date(2023, 6, 20)
        },
        {
            "ex_list_id": 8,
            "subject_id": 7,
            "grade": 89,
            "is_appeal": False,
            "record_date": date(2023, 6, 25)
        },
        {
            "ex_list_id": 8,
            "subject_id": 8,
            "grade": 95,
            "is_appeal": False,
            "record_date": date(2023, 6, 28)
        },
        {
            "ex_list_id": 8,
            "subject_id": 5,
            "grade": 87,
            "is_appeal": False,
            "record_date": date(2023, 7, 1)
        },

        # Абитуриент 9
        {
            "ex_list_id": 9,
            "subject_id": 2,
            "grade": 80,
            "is_appeal": False,
            "record_date": date(2023, 6, 20)
        },
        {
            "ex_list_id": 9,
            "subject_id": 7,
            "grade": 78,
            "is_appeal": False,
            "record_date": date(2023, 6, 25)
        },
        {
            "ex_list_id": 9,
            "subject_id": 8,
            "grade": 85,
            "is_appeal": False,
            "record_date": date(2023, 6, 28)
        },
        {
            "ex_list_id": 9,
            "subject_id": 5,
            "grade": 82,
            "is_appeal": False,
            "record_date": date(2023, 7, 1)
        },

        # Абитуриент 10
        {
            "ex_list_id": 10,
            "subject_id": 1,
            "grade": 90,
            "is_appeal": False,
            "record_date": date(2023, 6, 15)
        },
        {
            "ex_list_id": 10,
            "subject_id": 2,
            "grade": 86,
            "is_appeal": False,
            "record_date": date(2023, 6, 20)
        },
        {
            "ex_list_id": 10,
            "subject_id": 3,
            "grade": 88,
            "is_appeal": False,
            "record_date": date(2023, 6, 25)
        },
        {
            "ex_list_id": 10,
            "subject_id": 4,
            "grade": 92,
            "is_appeal": False,
            "record_date": date(2023, 6, 28)
        }
    ]
    yield "exam_record", exam_records

    stream_groups = [
        {"group_id": 1, "stream_id": 1},
        {"group_id": 2, "stream_id": 1},
        {"group_id": 3, "stream_id": 2},
        {"group_id": 4, "stream_id": 2},
        {"group_id": 5, "stream_id": 3},
        {"group_id": 6, "stream_id": 3},
        {"group_id": 7, "stream_id": 4},
        {"group_id": 8, "stream_id": 4},
        {"group_id": 9, "stream_id": 5},
        {"group_id": 10, "stream_id": 5}
    ]
    yield "stream_group", stream_groups

    exam_schedules = [
        {
            "stream_id": 1,
            "subject_id": 1,
            "classroom": "А-101",
            "exam_type": ExamType.CONSULTATION.value,
            "record_date": date(2023, 6, 14)
        },
        {
            "stream_id": 1,
            "subject_id": 1,
            "classroom": "А-101",
            "exam_type": ExamType.EXAM.value,
            "record_date": date(2023, 6, 15)
        },
        {
            "stream_id": 1,
            "subject_id": 2,
            "classroom": "Б-205",
            "exam_type": ExamType.CONSULTATION.value,
            "record_date": date(2023, 6, 19)
        },
        {
            "stream_id": 1,
            "subject_id": 2,
            "classroom": "Б-205",
            "exam_type": ExamType.EXAM.value,
            "record_date": date(2023, 6, 20)
        },
        {
            "stream_id": 1,
            "subject_id": 4,
            "classroom": "В-312",
            "exam_type": ExamType.CONSULTATION.value,
            "record_date": date(2023, 6, 24)
        },
        {
            "stream_id": 1,
            "subject_id": 4,
            "classroom": "В-312",
            "exam_type": ExamType.EXAM.value,
            "record_date": date(2023, 6, 25)
        },
        {
            "stream_id": 2,
            "subject_id": 1,
            "classroom": "Г-104",
            "exam_type": ExamType.CONSULTATION.value,
            "record_date": date(2023, 6, 14)
        },
        {
            "stream_id": 2,
            "subject_id": 1,
            "classroom": "Г-104",
            "exam_type": ExamType.EXAM.value,
            "record_date": date(2023, 6, 15)
        },
        {
            "stream_id": 2,
            "subject_id": 2,
            "classroom": "Д-201",
            "exam_type": ExamType.CONSULTATION.value,
            "record_date": date(2023, 6, 19)
        },
        {
            "stream_id": 2,
            "subject_id": 2,
            "classroom": "Д-201",
            "exam_type": ExamType.EXAM.value,
            "record_date": date(2023, 6, 20)
        },
        {
            "stream_id": 3,
            "subject_id": 2,
            "classroom": "А-102",
            "exam_type": ExamType.CONSULTATION.value,
            "record_date": date(2023, 6, 19)
        },
        {
            "stream_id": 3,
            "subject_id": 2,
            "classroom": "А-102",
            "exam_type": ExamType.EXAM.value,
            "record_date": date(2023, 6, 20)
        },
        {
            "stream_id": 3,
            "subject_id": 5,
            "classroom": "Б-301",
            "exam_type": ExamType.CONSULTATION.value,
            "record_date": date(2023, 6, 24)
        },
        {
            "stream_id": 3,
            "subject_id": 5,
            "classroom": "Б-301",
            "exam_type": ExamType.EXAM.value,
            "record_date": date(2023, 6, 25)
        },
        {
            "stream_id": 4,
            "subject_id": 2,
            "classroom": "В-215",
            "exam_type": ExamType.CONSULTATION.value,
            "record_date": date(2023, 6, 19)
        },
        {
            "stream_id": 4,
            "subject_id": 2,
            "classroom": "В-215",
            "exam_type": ExamType.EXAM.value,
            "record_date": date(2023, 6, 20)
        },
        {
            "stream_id": 4,
            "subject_id": 7,
            "classroom": "Г-305",
            "exam_type": ExamType.CONSULTATION.value,
            "record_date": date(2023, 6, 24)
        },
        {
            "stream_id": 4,
            "subject_id": 7,
            "classroom": "Г-305",
            "exam_type": ExamType.EXAM.value,
            "record_date": date(2023, 6, 25)
        },
        {
            "stream_id": 5,
            "subject_id": 1,
            "classroom": "Д-110",
            "exam_type": ExamType.CONSULTATION.value,
            "record_date": date(2023, 6, 14)
        },
        {
            "stream_id": 5,
            "subject_id": 1,
            "classroom": "Д-110",
            "exam_type": ExamType.EXAM.value,
            "record_date": date(2023, 6, 15)
        }
    ]

    yield "exam_schedule", exam_schedules