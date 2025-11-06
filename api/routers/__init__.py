from .faculty import router as faculty_router
from .group import router as group_router
from .root import router as root_router
from .abiturient import router as student_router

__all__ = [
    'faculty_router',
    'group_router',
    'root_router',
    'student_router'
]