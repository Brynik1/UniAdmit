from sqlalchemy.orm import Session
from .repositories import (
    FacultyRepository, DepartmentRepository, SchoolRepository,
    SubjectRepository, StudyGroupRepository, ExaminationListRepository,
    StreamRepository, AbiturientRepository, ExamRecordRepository,
    StreamGroupRepository, ExamScheduleRepository
)
from database.queries import (
    get_faculty_students, get_student_grades, get_student_subject_schedule,
    get_group_schedule, get_faculty_rating, get_faculty_avg_grades,
    get_faculties_with_students, get_students_sample, get_groups_sample,
    get_subjects_sample, get_schools
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

    def get_faculty_students(self, faculty_name: str, **kwargs):
        return get_faculty_students(faculty_name, self.session, **kwargs)

    def get_student_grades(self, last_name: str, first_name: str, **kwargs):
        return get_student_grades(last_name, first_name, self.session, **kwargs)

    def get_student_subject_schedule(self, last_name: str, first_name: str, subject_name: str, **kwargs):
        return get_student_subject_schedule(last_name, first_name, subject_name, self.session, **kwargs)

    def get_group_schedule(self, group_name: str, **kwargs):
        return get_group_schedule(group_name, self.session, **kwargs)

    def get_faculty_rating(self, faculty_name: str, **kwargs):
        return get_faculty_rating(faculty_name, self.session, **kwargs)

    def get_faculty_avg_grades(self, faculty_name: str, **kwargs):
        return get_faculty_avg_grades(faculty_name, self.session, **kwargs)


    # Metadata queries

    def get_faculties_with_students(self):
        return get_faculties_with_students(self.session)

    def get_students_sample(self):
        return get_students_sample(self.session)

    def get_groups_sample(self):
        return get_groups_sample(self.session)

    def get_subjects_sample(self):
        return get_subjects_sample(self.session)

    def get_schools(self, limit: int = None):
        return get_schools(self.session, limit)