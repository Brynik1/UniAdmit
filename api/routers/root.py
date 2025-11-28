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

    faculty_example = faculties_with_students[0].faculty_name if faculties_with_students else "Какая-то кафедра"
    abiturient_example = abiturients_sample[0]
    group_example = groups_sample[0].group_name if groups_sample else "Какая-то группа"
    subject_example = subjects_sample[0].subject_name if subjects_sample else "Какой-то предмет"

    return {
        "message": "🎓 Добро пожаловать в систему управления абитуриентами!",
        "description": "API для работы с базой данных абитуриентов университета",
        "endpoints": {
            "1.": {
                "path": "/faculty/{faculty_name}/abiturients",
                "description": "Получить всех абитуриентов указанного факультета",
                "example": f"/faculty/{faculty_example}/abiturients"
            },
            "2.": {
                "path": "/abiturient/{last_name}/{first_name}/grades",
                "description": "Получить все оценки абитуриента",
                "example": f"/abiturient/{abiturient_example.last_name}/{abiturient_example.first_name}/grades"
            },
            "3.": {
                "path": "/abiturient/{last_name}/{first_name}/schedule/{subject_name}",
                "description": "Получить расписание консультаций и экзаменов для абитуриента по предмету",
                "example": f"/abiturient/{abiturient_example.last_name}/{abiturient_example.first_name}/schedule/{subject_example}"
            },
            "4.": {
                "path": "/group/{group_name}/schedule",
                "description": "Получить расписание экзаменов для учебной группы",
                "example": f"/group/{group_example}/schedule"
            },
            "5.": {
                "path": "/faculty/{faculty_name}/rating",
                "description": "Получить рейтинг абитуриентов факультета по сумме баллов",
                "example": f"/faculty/{faculty_example}/rating"
            },
            "6.": {
                "path": "/faculty/{faculty_name}/avg-grades",
                "description": "Получить средний балл по предметам на факультете",
                "example": f"/faculty/{faculty_example}/avg-grades"
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