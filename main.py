import sys

from database import db_manager
from services.data import seeder
from services.demo import execute_all_queries
from core import config
from api import run_api



def prepare_db(db):
    db.drop_tables()
    db.create_tables()

def sample_seed(db):
    prepare_db(db)
    config.data.mode = 'sample'
    print(f"Заполнение базы данных в режиме sample")
    seeder.seed()

def bulk_seed(db):
    prepare_db(db)
    config.data.mode = 'bulk'
    print(f"Заполнение базы данных в режиме bulk")
    seeder.seed()


if __name__ == '__main__':
    args = sys.argv[1:]

    if '--sample' in args:
        sample_seed(db_manager)

    elif '--bulk' in args:
        bulk_seed(db_manager)

    elif '--demo' in args:
        if not db_manager.check_tables():
            sample_seed(db_manager)

        execute_all_queries()

    elif '--api' in args:
        if not db_manager.check_tables():
            sample_seed(db_manager)

        run_api()



