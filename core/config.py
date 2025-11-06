import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass
class DatabaseConfig:
    """Конфигурация базы данных"""
    host: str
    port: str
    name: str
    user: str
    password: str

    @property
    def connection_string(self):
        """Строка подключения к PostgreSQL"""
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


@dataclass
class APIConfig:
    """Конфигурация API"""
    host: str
    port: int
    reload: bool


@dataclass
class DataConfig:
    """Конфигурация генерации данных"""
    mode: str  # 'sample' | 'bulk'
    abiturient_count: int
    faculty_count: int
    school_count: int
    group_count: int
    stream_count: int
    subject_count: int
    batch_size: int


@dataclass
class AppConfig:
    """Основная конфигурация приложения"""
    database: DatabaseConfig
    api: APIConfig
    data: DataConfig


def load_config() -> AppConfig:
    """Загрузка конфигурации из переменных окружения"""

    # Конфигурация бд
    db_config = DatabaseConfig(
        host=os.getenv('DB_HOST', 'localhost'),
        port=os.getenv('DB_PORT', '5432'),
        name=os.getenv('DB_NAME', 'university_db'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASSWORD', 'password')
    )

    # Конфигурация API
    api_config = APIConfig(
        host=os.getenv('API_HOST', '0.0.0.0'),
        port=int(os.getenv('API_PORT', '8000')),
        reload=os.getenv('API_RELOAD', 'false').lower() == 'true'
    )

    # Конфигурация генератора данных
    data_config = DataConfig(
        mode=os.getenv('DATA_MODE', 'sample'),
        abiturient_count=int(os.getenv('DATA_ABITURIENT_COUNT', '10')),
        faculty_count=int(os.getenv('DATA_FACULTY_COUNT', '10')),
        school_count=int(os.getenv('DATA_SCHOOL_COUNT', '10')),
        group_count=int(os.getenv('DATA_GROUP_COUNT', '10')),
        stream_count=int(os.getenv('DATA_STREAM_COUNT', '10')),
        subject_count=int(os.getenv('DATA_SUBJECT_COUNT', '10')),
        batch_size=int(os.getenv('DATA_BATCH_SIZE', '1000'))
    )

    return AppConfig(
        database=db_config,
        api=api_config,
        data=data_config,
    )


# Глобальный экземпляр конфигурации
config = load_config()