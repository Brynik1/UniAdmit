import uvicorn
from core import config
from fastapi import FastAPI

from api.middleware import add_charset_header
from api.routers import faculty_router, group_router, root_router, student_router


def create_app():
    app = FastAPI(
        title="🎓 Система управления абитуриентами",
        description="API для работы с базой данных абитуриентов",
        version="1.0.0"
    )

    app.middleware("http")(add_charset_header)

    app.include_router(root_router)
    app.include_router(group_router)
    app.include_router(faculty_router)
    app.include_router(student_router)

    return app


def run_api():
    """Запуск API сервера"""
    app = create_app()

    uvicorn.run(
        app=app,
        host=config.api.host,
        port=config.api.port,
        reload=False
    )

if __name__ == '__main__':
    run_api()