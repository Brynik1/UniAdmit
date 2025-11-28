from fastapi import APIRouter, Depends, HTTPException

from database import MainRepository
from api.di import get_repository

router = APIRouter(prefix="/group", tags=["groups"])


@router.get("/schedule")
async def get_group_schedule(
    group_name: str,
    repo: MainRepository = Depends(get_repository)
):
    """Получить расписание экзаменов для учебной группы"""
    try:
        results = repo.get_group_schedule(group_name)

        if not results:
            raise HTTPException(
                status_code=404,
                detail=f"Расписание для группы '{group_name}' не найдено"
            )

        schedule = []
        for row in results:
            schedule.append({
                "date": row.schedule_date.isoformat() if row.schedule_date else None,
                "classroom": row.classroom,
                "subject": row.subject_name,
                "type": row.Тип
            })

        return {
            "group": group_name,
            "count": len(schedule),
            "schedule": schedule
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Ошибка сервера: {str(e)}")