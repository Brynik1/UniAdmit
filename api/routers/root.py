from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.queries import (
    get_faculties_with_students,
    get_students_sample,
    get_groups_sample,
    get_subjects_sample,
    get_faculties_count,
    get_students_count,
    get_groups_count,
    get_subjects_count
)
from database import db_manager

router = APIRouter(tags=["root"])


@router.get("/")
async def root_api(db: Session = Depends(db_manager.get_db)):
    """Корневой эндпоинт с информацией о API и примерами запросов"""

    # Получаем примеры данных
    faculties_with_students = get_faculties_with_students(db)
    students_sample = get_students_sample(db)
    groups_sample = get_groups_sample(db)
    subjects_sample = get_subjects_sample(db)

    # Генерируем динамические примеры URL на основе реальных данных
    faculty_example = faculties_with_students[0][0] if faculties_with_students else "Факультет компьютерных технологий"
    student_example = students_sample[0] if students_sample else ("Иванов", "Алексей")
    group_example = groups_sample[0][0] if groups_sample else "ПИ-101"
    subject_example = subjects_sample[0][0] if subjects_sample else "Математика"

    example_urls = {
        "faculty_abiturients": f"/faculty/{faculty_example}/abiturients",
        "student_grades": f"/student/{student_example[0]}/{student_example[1]}/grades",
        "student_schedule": f"/student/{student_example[0]}/{student_example[1]}/schedule/{subject_example}",
        "group_schedule": f"/group/{group_example}/schedule",
        "faculty_rating": f"/faculty/{faculty_example}/rating",
        "faculty_avg_grades": f"/faculty/{faculty_example}/avg-grades"
    }

    # Статистика
    statistics = {
        "total_faculties": get_faculties_count(db),
        "total_students": get_students_count(db),
        "total_groups": get_groups_count(db),
        "total_subjects": get_subjects_count(db)
    }

    # Примеры доступных данных
    examples = {
        "available_faculties": [f[0] for f in faculties_with_students[:3]],
        "available_students": [{"last_name": s[0], "first_name": s[1]} for s in students_sample[:3]],
        "available_groups": [g[0] for g in groups_sample[:3]],
        "available_subjects": [s[0] for s in subjects_sample[:3]]
    }

    return {
        "message": "🎓 Добро пожаловать в систему управления абитуриентами!",
        "description": "API для работы с базой данных абитуриентов университета",
        "endpoints": {
            "1.": {
                "path": "/faculty/{faculty_name}/abiturients",
                "description": "Получить всех абитуриентов указанного факультета",
                "example": example_urls["faculty_abiturients"]
            },
            "2.": {
                "path": "/student/{last_name}/{first_name}/grades",
                "description": "Получить все оценки абитуриента",
                "example": example_urls["student_grades"]
            },
            "3.": {
                "path": "/student/{last_name}/{first_name}/schedule/{subject_name}",
                "description": "Получить расписание консультаций и экзаменов для абитуриента по предмету",
                "example": example_urls["student_schedule"]
            },
            "4.": {
                "path": "/group/{group_name}/schedule",
                "description": "Получить расписание экзаменов для учебной группы",
                "example": example_urls["group_schedule"]
            },
            "5.": {
                "path": "/faculty/{faculty_name}/rating",
                "description": "Получить рейтинг абитуриентов факультета по сумме баллов",
                "example": example_urls["faculty_rating"]
            },
            "6.": {
                "path": "/faculty/{faculty_name}/avg-grades",
                "description": "Получить средний балл по предметам на факультете",
                "example": example_urls["faculty_avg_grades"]
            },
            "7.": {
                "path": "/",
                "description": "Корневой эндпоинт (текущее окно)",
            }
        },
        "examples": examples,
        "statistics": statistics
    }