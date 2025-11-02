from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import db_manager, MainRepository

router = APIRouter(prefix="/group", tags=["groups"])


@router.get("/{group_name}/schedule")
async def get_group_schedule_api(
    group_name: str,
    db: Session = Depends(db_manager.get_db)
):
    """Получить расписание экзаменов для учебной группы"""
    try:
        repo = MainRepository(db)
        results = repo.get_group_schedule(group_name)

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