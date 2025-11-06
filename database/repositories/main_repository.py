from sqlalchemy.orm import Session
from .child_repositories import (
    FacultyRepository, DepartmentRepository, SchoolRepository,
    SubjectRepository, StudyGroupRepository, ExaminationListRepository,
    StreamRepository, AbiturientRepository, ExamRecordRepository,
    StreamGroupRepository, ExamScheduleRepository
)
from database.queries import (
    get_faculty_students, get_student_grades, get_student_subject_schedule,
    get_group_schedule, get_faculty_rating, get_faculty_avg_grades
)


class MainRepository:
    """
    Основной репозиторий, который управляет всеми дочерними репозиториями
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

    def get_faculty_students(self, faculty_name, sort=False, limit=None):
        return get_faculty_students(faculty_name, self.session, sort, limit)

    def get_student_grades(self, last_name, first_name, sort=False, limit=None):
        return get_student_grades(last_name, first_name, self.session, sort, limit)

    def get_student_subject_schedule(self, last_name, first_name: str, subject_name: str, sort=False, limit=None):
        return get_student_subject_schedule(last_name, first_name, subject_name, self.session, sort, limit)

    def get_group_schedule(self, group_name, sort=False, limit=None):
        return get_group_schedule(group_name, self.session, sort, limit)

    def get_faculty_rating(self, faculty_name, sort=False, limit=None):
        return get_faculty_rating(faculty_name, self.session, sort, limit)

    def get_faculty_avg_grades(self, faculty_name, sort=False, limit=None):
        return get_faculty_avg_grades(faculty_name, self.session, sort, limit)
