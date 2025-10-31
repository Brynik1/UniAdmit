from .complex_queries import (
    get_faculty_students,
    get_student_grades,
    get_student_subject_schedule,
    get_group_schedule,
    get_faculty_rating,
    get_faculty_avg_grades
)

from .metadata_queries import (
    get_faculties_with_students,
    get_students_sample,
    get_groups_sample,
    get_subjects_sample,
    get_faculties_count,
    get_students_count,
    get_groups_count,
    get_subjects_count,
    get_schools,
    create_school,
    update_school,
    delete_school
)

__all__ = [
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
    'get_faculties_count',
    'get_students_count',
    'get_groups_count',
    'get_subjects_count',
    'get_schools',
    'create_school',
    'update_school',
    'delete_school'
]