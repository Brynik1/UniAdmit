import uvicorn
from core import config
from fastapi import FastAPI
from api.router import router


def create_app():
    app = FastAPI(
        title="🎓 Система управления абитуриентами",
        description="API для работы с базой данных абитуриентов",
        version="1.0.0"
    )
    app.include_router(router)

    return app


def run_api():
    """Запуск API сервера"""
    app = create_app()

    uvicorn.run(
        app,
        host=config.api.host,
        port=config.api.port,
        reload=False
    )

if __name__ == '__main__':
    run_api()