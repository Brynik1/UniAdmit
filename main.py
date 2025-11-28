import sys

from database import db_manager
from services.benchmarks import DatabaseBenchmark
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

    if '--bench' in args:
        benchmark = DatabaseBenchmark(
            test_sizes=[100, 1000, 10_000, 100_000, 1_000_000],
            sort=True,
            limit=5
        )
        benchmark.run_benchmark()

