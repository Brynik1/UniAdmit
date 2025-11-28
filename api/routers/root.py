from fastapi import APIRouter, Depends

from database import MainRepository
from api.di import get_repository

router = APIRouter(tags=["root"])


@router.get("/")
async def root(repo: MainRepository = Depends(get_repository)):
    """Корневой эндпоинт с информацией о API и примерами запросов"""

    # Получаем примеры данных
    faculties_with_students = repo.faculty.get_sample(limit=3)
    abiturients_sample = repo.abiturient.get_sample(limit=3)
    groups_sample = repo.study_group.get_sample(limit=3)
    subjects_sample = repo.subject.get_sample(limit=3)

    return {
        "message": "🎓 Добро пожаловать в систему управления абитуриентами!",
        "description": "API для работы с базой данных абитуриентов университета",
        "endpoints": {
            "1.": {
                "path": "/faculty/abiturients",
                "description": "Получить всех абитуриентов указанного факультета",
            },
            "2.": {
                "path": "/abiturient/grades",
                "description": "Получить все оценки абитуриента",
            },
            "3.": {
                "path": "/abiturient/schedule",
                "description": "Получить расписание консультаций и экзаменов для абитуриента по предмету",
            },
            "4.": {
                "path": "/group/schedule",
                "description": "Получить расписание экзаменов для учебной группы",
            },
            "5.": {
                "path": "/faculty/rating",
                "description": "Получить рейтинг абитуриентов факультета по сумме баллов",
            },
            "6.": {
                "path": "/faculty/avg-grades",
                "description": "Получить средний балл по предметам на факультете",
            },
            "7.": {
                "path": "/",
                "description": "Корневой эндпоинт (текущее окно)",
            }
        },

        "examples": {
            "available_faculties": [f.faculty_name for f in faculties_with_students[:3]],
            "available_abiturients": [f"{s.last_name} {s.first_name}" for s in abiturients_sample[:3]],
            "available_groups": [g.group_name for g in groups_sample[:3]],
            "available_subjects": [s.subject_name for s in subjects_sample[:3]]
        },

        "statistics": {
            "total_faculties": repo.faculty.get_count(),
            "total_abiturients": repo.abiturient.get_count(),
            "total_groups": repo.study_group.get_count(),
            "total_subjects": repo.subject.get_count()
        }
    }