from database import db_manager
from .data.sample_data import generate_sample_data
from .data.bulk_data import generate_bulk_data
from core import config

from database.repositories import (
    FacultyRepository, DepartmentRepository, SchoolRepository,
    SubjectRepository, StudyGroupRepository, ExaminationListRepository,
    StreamRepository, AbiturientRepository, ExamRecordRepository,
    StreamGroupRepository, ExamScheduleRepository
)


class Seeder:
    def __init__(self):
        self.repositories = {
            'faculty': FacultyRepository,
            'department': DepartmentRepository,
            'school': SchoolRepository,
            'subject': SubjectRepository,
            'study_group': StudyGroupRepository,
            'examination_list': ExaminationListRepository,
            'stream': StreamRepository,
            'abiturient': AbiturientRepository,
            'exam_record': ExamRecordRepository,
            'stream_group': StreamGroupRepository,
            'exam_schedule': ExamScheduleRepository
        }
        self.data_config = config.data

    def seed(self):
        """
        Основной метод для заполнения базы данных
        """
        if self.data_config.mode == 'sample':
            data_generator = generate_sample_data()
        else:
            data_generator = generate_bulk_data(
                student_count=self.data_config.student_count,
                faculty_count=self.data_config.faculty_count,
                school_count=self.data_config.school_count,
                group_count=self.data_config.group_count,
                stream_count=self.data_config.stream_count,
                subject_count=self.data_config.subject_count,
                batch_size=self.data_config.batch_size
            )

        with db_manager.get_session() as session:
            repos = {name: repo_class(session) for name, repo_class in self.repositories.items()}

            for item in data_generator:
                table_name, data = item

                if table_name in repos:
                    repo = repos[table_name]

                    # Если data - это список записей
                    if isinstance(data, list):
                        repo.bulk_create(data)

                    # Если data - это одна запись (словарь)
                    elif isinstance(data, dict):
                        repo.create(**data)



# Создаем глобальный экземпляр сидера
seeder = Seeder()