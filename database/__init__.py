from .database_manager import (
    DatabaseManager,
    db_manager
)

from .queries import (
    # Complex queries
    get_faculty_students,
    get_student_grades,
    get_student_subject_schedule,
    get_group_schedule,
    get_faculty_rating,
    get_faculty_avg_grades,

    # Metadata queries
    get_faculties_with_students,
    get_students_sample,
    get_groups_sample,
    get_subjects_sample,
)

from .repositories import (
    FacultyRepository,
    DepartmentRepository,
    SchoolRepository,
    SubjectRepository,
    StudyGroupRepository,
    ExaminationListRepository,
    StreamRepository,
    AbiturientRepository,
    ExamRecordRepository,
    StreamGroupRepository,
    ExamScheduleRepository
)

__all__ = [
    # Database management
    'DatabaseManager',
    'db_manager',

    # Queries
    'get_faculty_students',
    'get_student_grades',
    'get_student_subject_schedule',
    'get_group_schedule',
    'get_faculty_rating',
    'get_faculty_avg_grades',
    'get_faculties_with_students',
    'get_students_sample',
    'get_groups_sample',
    'get_subjects_sample',

    # Repositories
    'FacultyRepository',
    'DepartmentRepository',
    'SchoolRepository',
    'SubjectRepository',
    'StudyGroupRepository',
    'ExaminationListRepository',
    'StreamRepository',
    'AbiturientRepository',
    'ExamRecordRepository',
    'StreamGroupRepository',
    'ExamScheduleRepository'
]