from sqlalchemy.orm import Session
from sqlalchemy import func, case, literal

from .child_repositories import (
    FacultyRepository, DepartmentRepository, SchoolRepository,
    SubjectRepository, StudyGroupRepository, ExaminationListRepository,
    StreamRepository, AbiturientRepository, ExamRecordRepository,
    StreamGroupRepository, ExamScheduleRepository
)
from database.models import (
    Faculty, Department, Abiturient,
    Subject, ExamRecord, ExamSchedule, StudyGroup,
    ExaminationList, Stream, StreamGroup, MedalType, ExamType
)


class MainRepository:
    """
    Основной репозиторий, который управляет всеми дочерними
    и предоставляет доступ к запросам
    """

    def __init__(self, session: Session):
        self.session = session

        # Инициализируем все дочерние репозитории
        self.faculty = FacultyRepository(session)
        self.department = DepartmentRepository(session)
        self.school = SchoolRepository(session)
        self.subject = SubjectRepository(session)
        self.study_group = StudyGroupRepository(session)
        self.examination_list = ExaminationListRepository(session)
        self.stream = StreamRepository(session)
        self.abiturient = AbiturientRepository(session)
        self.exam_record = ExamRecordRepository(session)
        self.stream_group = StreamGroupRepository(session)
        self.exam_schedule = ExamScheduleRepository(session)

    # Complex queries

    def get_faculty_abiturients(
            self,
            faculty_name: str,
            sort: bool = False,
            limit: int = None
    ):
        """Получить абитуриентов факультета"""
        query = self.session.query(
            Abiturient.last_name.label("Фамилия"),
            Abiturient.first_name.label("Имя"),
            Abiturient.patronymic.label("Отчество"),
            Faculty.name.label("Факультет"),
            Department.name.label("Кафедра"),
            case(
                (Abiturient.is_enrolled == True, "Да"), else_="Нет"
            ).label("Зачислен")
        ).join(Department, Abiturient.department_id == Department.id) \
            .join(Faculty, Department.faculty_id == Faculty.id) \
            .filter(Faculty.name == faculty_name)

        if sort:
            query = query.order_by(
                Abiturient.last_name,
                Abiturient.first_name,
                Abiturient.patronymic
            )

        return query.limit(limit).all() if limit else query.all()

    def get_abiturient_grades(
            self,
            last_name: str,
            first_name: str,
            sort: bool = False,
            limit: int = None
    ):
        """Получить оценки абитуриента"""
        query = self.session.query(
            Subject.name.label("Предмет"),
            ExamRecord.grade.label("Оценка"),
            ExamRecord.record_date.label("Дата_экзамена"),
            case(
                (ExamRecord.is_appeal == True, "Да"), else_="Нет"
            ).label("Апелляция")
        ).join(ExaminationList, ExamRecord.ex_list_id == ExaminationList.id) \
            .join(Abiturient, ExaminationList.id == Abiturient.ex_list_id) \
            .join(Subject, ExamRecord.subject_id == Subject.id) \
            .filter(Abiturient.last_name == last_name, Abiturient.first_name == first_name)

        if sort:
            query = query.order_by(
                ExamRecord.record_date
            )

        return query.limit(limit).all() if limit else query.all()

    def get_abiturient_subject_schedule(
            self,
            last_name: str,
            first_name: str,
            subject_name: str,
            sort: bool = False,
            limit: int = None
    ):
        """Получить расписание консультаций и экзаменов для абитуриента по предмету"""
        query = self.session.query(
            ExamSchedule.record_date.label("Дата"),
            ExamSchedule.classroom.label("Аудитория"),
            case(
                (ExamSchedule.exam_type == ExamType.CONSULTATION, "Консультация"),
                (ExamSchedule.exam_type == ExamType.EXAM, "Экзамен"),
                else_="Неизвестно"
            ).label("Тип"),
            Subject.name.label("Предмет")
        ).join(Subject, ExamSchedule.subject_id == Subject.id) \
            .join(Stream, ExamSchedule.stream_id == Stream.id) \
            .join(StreamGroup, Stream.id == StreamGroup.stream_id) \
            .join(StudyGroup, StreamGroup.group_id == StudyGroup.id) \
            .join(ExaminationList, StudyGroup.id == ExaminationList.group_id) \
            .join(Abiturient, ExaminationList.id == Abiturient.ex_list_id) \
            .filter(
            Abiturient.last_name == last_name,
            Abiturient.first_name == first_name,
            Subject.name == subject_name
        )

        if sort:
            query = query.order_by(
                ExamSchedule.record_date
            )

        return query.limit(limit).all() if limit else query.all()

    def get_group_schedule(
            self,
            group_name: str,
            sort: bool = False,
            limit: int = None
    ):
        """Получить расписание экзаменов для учебной группы"""
        query = self.session.query(
            ExamSchedule.record_date.label("Дата"),
            ExamSchedule.classroom.label("Аудитория"),
            Subject.name.label("Предмет"),
            literal("Экзамен").label("Тип")
        ).join(Subject, ExamSchedule.subject_id == Subject.id) \
            .join(Stream, ExamSchedule.stream_id == Stream.id) \
            .join(StreamGroup, Stream.id == StreamGroup.stream_id) \
            .join(StudyGroup, StreamGroup.group_id == StudyGroup.id) \
            .filter(
            StudyGroup.name == group_name,
            ExamSchedule.exam_type == ExamType.EXAM
        )

        if sort:
            query = query.order_by(
                ExamSchedule.record_date
            )

        return query.limit(limit).all() if limit else query.all()

    def get_faculty_rating(
            self,
            faculty_name: str,
            sort: bool = False,
            limit: int = None
    ):
        """Получить рейтинг абитуриентов факультета по сумме баллов"""
        query = self.session.query(
            Abiturient.last_name.label("Фамилия"),
            Abiturient.first_name.label("Имя"),
            case(
                (Abiturient.has_medal == MedalType.GOLD, "Золотая"),
                (Abiturient.has_medal == MedalType.SILVER, "Серебряная"),
                else_="Нет"
            ).label("Медаль"),
            func.sum(ExamRecord.grade).label("Сумма_баллов")
        ).join(Department, Abiturient.department_id == Department.id) \
            .join(Faculty, Department.faculty_id == Faculty.id) \
            .join(ExaminationList, Abiturient.ex_list_id == ExaminationList.id) \
            .join(ExamRecord, ExaminationList.id == ExamRecord.ex_list_id) \
            .filter(Faculty.name == faculty_name) \
            .group_by(Abiturient.id, Abiturient.last_name, Abiturient.first_name, Abiturient.has_medal)

        if sort:
            query = query.order_by(
                func.sum(ExamRecord.grade).desc()
            )

        return query.limit(limit).all() if limit else query.all()

    def get_faculty_avg_grades(
            self,
            faculty_name: str,
            sort: bool = False,
            limit: int = None
    ):
        """Получить средний балл по предметам на факультете"""
        query = self.session.query(
            Subject.name.label("Предмет"),
            func.round(func.avg(ExamRecord.grade), 2).label("Средний_балл")
        ).join(ExamRecord, Subject.id == ExamRecord.subject_id) \
            .join(ExaminationList, ExamRecord.ex_list_id == ExaminationList.id) \
            .join(Abiturient, ExaminationList.id == Abiturient.ex_list_id) \
            .join(Department, Abiturient.department_id == Department.id) \
            .join(Faculty, Department.faculty_id == Faculty.id) \
            .filter(Faculty.name == faculty_name) \
            .group_by(Subject.id, Subject.name)

        if sort:
            query = query.order_by(
                func.avg(ExamRecord.grade)
            )

        return query.limit(limit).all() if limit else query.all()