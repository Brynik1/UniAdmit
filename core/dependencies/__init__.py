from .api_di import get_main_repository as get_repo
from .services_di import get_main_repository as context_repo

__all__ = ['get_repo', 'context_repo']