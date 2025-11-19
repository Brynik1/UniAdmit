from fastapi import APIRouter, Depends, HTTPException

from database import MainRepository
from api.di import get_repository

router = APIRouter(prefix="/abiturient", tags=["abiturients"])


@router.get("/{last_name}/{first_name}/grades")
async def get_abiturient_grades_api(
    last_name: str,
    first_name: str,
    repo: MainRepository = Depends(get_repository)
):
    """Получить все оценки абитуриента"""
    try:
        results = repo.get_abiturient_grades(last_name, first_name)

        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Абитуриент {last_name} {first_name} не найден или у него нет оценок"
            )

        grades = []
        for row in results:
            grades.append({
                "subject": row.subject_name,
                "grade": row.grade,
                "exam_date": row.exam_date.isoformat() if row.exam_date else None,
                "is_appeal": row.Апелляция == "Да"
            })

        return {
            "abiturient": f"{last_name} {first_name}",
            "count": len(grades),
            "grades": grades
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")


@router.get("/{last_name}/{first_name}/schedule/{subject_name}")
async def get_abiturient_subject_schedule_api(
    last_name: str,
    first_name: str,
    subject_name: str,
    repo: MainRepository = Depends(get_repository)
):
    """Получить расписание консультаций и экзаменов для абитуриента по предмету"""
    try:
        results = repo.get_abiturient_subject_schedule(last_name, first_name, subject_name)

        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Расписание для абитуриента {last_name} {first_name} по предмету '{subject_name}' не найдено"
            )

        schedule = []
        for row in results:
            schedule.append({
                "date": row.schedule_date.isoformat() if row.schedule_date else None,
                "classroom": row.classroom,
                "type": row.Тип,
                "subject": row.subject_name
            })

        return {
            "abiturient": f"{last_name} {first_name}",
            "subject": subject_name,
            "count": len(schedule),
            "schedule": schedule
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")