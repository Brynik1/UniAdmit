import sys
from database import db_manager
from services.data import seeder
from services.demo import execute_all_queries
from core import config
from api import run_api


if __name__ == '__main__':
    args = sys.argv[1:]

    if '--sample' in args or '--bulk' in args:
        db_manager.drop_tables()
        db_manager.create_tables()
        if '-sample' in args:
            config.data.mode = 'sample'
        elif '--bulk' in args:
            config.data.mode = 'bulk'

        print(f"Заполнение базы данных в режиме: {config.data.mode}")
        seeder.seed()

    if '--demo' in args:
        execute_all_queries()

    if '--api' in args:
        run_api()
