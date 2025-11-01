from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.queries import (
    get_faculty_students,
    get_faculty_rating,
    get_faculty_avg_grades
)
from database import db_manager

router = APIRouter(prefix="/faculty", tags=["faculties"])


@router.get("/{faculty_name}/abiturients")
async def get_faculty_students_api(
    faculty_name: str,
    db: Session = Depends(db_manager.get_db)
):
    """Получить всех абитуриентов указанного факультета"""
    try:
        results = get_faculty_students(faculty_name, db)

        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Факультет '{faculty_name}' не найден или на нем нет абитуриентов"
            )

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


@router.get("/{faculty_name}/rating")
async def get_faculty_rating_api(
    faculty_name: str,
    db: Session = Depends(db_manager.get_db)
):
    """Получить рейтинг абитуриентов факультета по сумме баллов"""
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


@router.get("/{faculty_name}/avg-grades")
async def get_faculty_avg_grades_api(
    faculty_name: str,
    db: Session = Depends(db_manager.get_db)
):
    """Получить средний балл по предметам на факультете"""
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