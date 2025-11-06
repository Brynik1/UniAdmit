from services.context_db import get_repository
from .generators.sample_data import generate_sample_data
from .generators.bulk_data import generate_bulk_data
from core import config


class Seeder:
    def __init__(self):
        self.data_config = config.data

    def seed(self):
        """
        Основной метод для заполнения базы данных
        """
        if self.data_config.mode == 'sample':
            data_generator = generate_sample_data()
        else:
            data_generator = generate_bulk_data(
                abiturient_count=self.data_config.abiturient_count,
                faculty_count=self.data_config.faculty_count,
                school_count=self.data_config.school_count,
                group_count=self.data_config.group_count,
                stream_count=self.data_config.stream_count,
                subject_count=self.data_config.subject_count,
                batch_size=self.data_config.batch_size
            )

        with get_repository() as repo:

            for (table_name, data) in data_generator:

                child_repo = getattr(repo, table_name)
                child_repo.bulk_create(data)


# Создаем глобальный экземпляр сидера
seeder = Seeder()