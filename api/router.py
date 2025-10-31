from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from database import db_manager
from database.queries import (
    get_faculty_students,
    get_student_grades,
    get_student_subject_schedule,
    get_group_schedule,
    get_faculty_rating,
    get_faculty_avg_grades,

    # Служебные запросы
    get_faculties_with_students,
    get_students_sample,
    get_groups_sample,
    get_subjects_sample,
    get_faculties_count,
    get_students_count,
    get_groups_count,
    get_subjects_count
)

# Создаем роутер
router = APIRouter()


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


@router.get("/faculty/{faculty_name}/abiturients")
async def get_faculty_students_api(
        faculty_name: str,
        db: Session = Depends(db_manager.get_db)
):
    """
    Получить всех абитуриентов указанного факультета
    """
    try:
        results = get_faculty_students(faculty_name, db)

        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Факультет '{faculty_name}' не найден или на нем нет абитуриентов"
            )

        # Преобразуем результаты в словарь
        abiturients = []
        for row in results:
            abiturients.append({
                "last_name": row.Фамилия,
                "first_name": row.Имя,
                "patronymic": row.Отчество,
                "faculty": row.Факультет,
                "department": row.Кафедра,
                "is_enrolled": row.Зачислен == "Да"
            })

        return {
            "faculty": faculty_name,
            "count": len(abiturients),
            "abiturients": abiturients
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.get("/student/{last_name}/{first_name}/grades")
async def get_student_grades_api(
        last_name: str,
        first_name: str,
        db: Session = Depends(db_manager.get_db)
):
    """
    Получить все оценки абитуриента
    """
    try:
        results = get_student_grades(last_name, first_name, db)

        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Абитуриент {last_name} {first_name} не найден или у него нет оценок"
            )

        grades = []
        for row in results:
            grades.append({
                "subject": row.Предмет,
                "grade": row.Оценка,
                "exam_date": row.Дата_экзамена.isoformat() if row.Дата_экзамена else None,
                "is_appeal": row.Апелляция == "Да"
            })

        return {
            "student": f"{last_name} {first_name}",
            "count": len(grades),
            "grades": grades
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.get("/student/{last_name}/{first_name}/schedule/{subject_name}")
async def get_student_subject_schedule_api(
        last_name: str,
        first_name: str,
        subject_name: str,
        db: Session = Depends(db_manager.get_db)
):
    """
    Получить расписание консультаций и экзаменов для абитуриента по предмету
    """
    try:
        results = get_student_subject_schedule(last_name, first_name, subject_name, db)

        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Расписание для абитуриента {last_name} {first_name} по предмету '{subject_name}' не найдено"
            )

        schedule = []
        for row in results:
            schedule.append({
                "date": row.Дата.isoformat() if row.Дата else None,
                "classroom": row.Аудитория,
                "type": row.Тип,
                "subject": row.Предмет
            })

        return {
            "student": f"{last_name} {first_name}",
            "subject": subject_name,
            "count": len(schedule),
            "schedule": schedule
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.get("/group/{group_name}/schedule")
async def get_group_schedule_api(
        group_name: str,
        db: Session = Depends(db_manager.get_db)
):
    """
    Получить расписание экзаменов для учебной группы
    """
    try:
        results = get_group_schedule(group_name, db)

        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Расписание для группы '{group_name}' не найдено"
            )

        schedule = []
        for row in results:
            schedule.append({
                "date": row.Дата.isoformat() if row.Дата else None,
                "classroom": row.Аудитория,
                "subject": row.Предмет,
                "type": row.Тип
            })

        return {
            "group": group_name,
            "count": len(schedule),
            "schedule": schedule
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.get("/faculty/{faculty_name}/rating")
async def get_faculty_rating_api(
        faculty_name: str,
        db: Session = Depends(db_manager.get_db)
):
    """
    Получить рейтинг абитуриентов факультета по сумме баллов
    """
    try:
        results = get_faculty_rating(faculty_name, db)

        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Рейтинг для факультета '{faculty_name}' не найден"
            )

        rating = []
        for i, row in enumerate(results, 1):
            rating.append({
                "position": i,
                "last_name": row.Фамилия,
                "first_name": row.Имя,
                "medal": row.Медаль,
                "total_score": float(row.Сумма_баллов) if row.Сумма_баллов else 0
            })

        return {
            "faculty": faculty_name,
            "count": len(rating),
            "rating": rating
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.get("/faculty/{faculty_name}/avg-grades")
async def get_faculty_avg_grades_api(
        faculty_name: str,
        db: Session = Depends(db_manager.get_db)
):
    """
    Получить средний балл по предметам на факультете
    """
    try:
        results = get_faculty_avg_grades(faculty_name, db)

        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Средние баллы для факультета '{faculty_name}' не найдены"
            )

        avg_grades = []
        for row in results:
            avg_grades.append({
                "subject": row.Предмет,
                "avg_grade": float(row.Средний_балл) if row.Средний_балл else 0
            })

        return {
            "faculty": faculty_name,
            "count": len(avg_grades),
            "average_grades": avg_grades
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")