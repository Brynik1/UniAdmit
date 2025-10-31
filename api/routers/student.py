from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database.queries import (
    get_student_grades,
    get_student_subject_schedule
)
from database import db_manager

router = APIRouter(prefix="/student", tags=["students"])


@router.get("/{last_name}/{first_name}/grades")
async def get_student_grades_api(
    last_name: str,
    first_name: str,
    db: Session = Depends(db_manager.get_db)
):
    """Получить все оценки абитуриента"""
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


@router.get("/{last_name}/{first_name}/schedule/{subject_name}")
async def get_student_subject_schedule_api(
    last_name: str,
    first_name: str,
    subject_name: str,
    db: Session = Depends(db_manager.get_db)
):
    """Получить расписание консультаций и экзаменов для абитуриента по предмету"""
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