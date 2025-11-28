from time import perf_counter
from typing import Dict, List, Any, Optional

from database import db_manager
from services.data import seeder
from services.context_db import get_repository
from core import config


class DatabaseBenchmark:
    """Класс для проведения бенчмарков базы данных"""

    def __init__(
            self,
            test_sizes: List[int] = None,
            sort: bool = True,
            limit: int = 5
    ):
        self.test_sizes = test_sizes or [100, 1000, 10_000]
        self.sort = sort
        self.limit = limit
        self.benchmark_results: Dict[str, Dict[int, float]] = {}
        self._test_data: Optional[Dict[str, Any]] = None

    def prepare_db(self, size: int) -> None:
        """Подготовка базы данных с заданным размером"""
        db_manager.drop_tables()
        db_manager.create_tables()

        config.data.mode = 'bulk'
        config.data.abiturient_count = size
        config.data.faculty_count = size
        config.data.school_count = size
        config.data.group_count = size
        config.data.stream_count = size
        config.data.subject_count = size
        config.data.batch_size = min(1000, size // 10)

        seeder.seed()

    def _get_test_data(self) -> Dict[str, Any]:
        """Получение тестовых данных из базы"""
        test_data = {}

        with get_repository() as repo:
            faculty_sample = repo.faculty.get_sample()
            test_data['faculty'] = faculty_sample.faculty_name

            abiturient_sample = repo.abiturient.get_sample()
            test_data['abiturient'] = {
                'last_name': abiturient_sample.last_name,
                'first_name': abiturient_sample.first_name
            }

            group_sample = repo.study_group.get_sample()
            test_data['group'] = group_sample.group_name

            subject_sample = repo.subject.get_sample()
            test_data['subject'] = subject_sample.subject_name

        return test_data

    def measure_time(self, repo_method: str, *args, **kwargs) -> float:
        """Измерение среднего времени выполнения метода"""
        sum_times = 0.0

        for _ in range(5):
            start_time = perf_counter()

            with get_repository() as repo:
                method = getattr(repo, repo_method)
                method(*args, **kwargs)

            sum_times += (perf_counter() - start_time) * 1000

        return sum_times / 5

    def _get_queries(self) -> List[Dict[str, Any]]:
        """Получение списка тестовых запросов"""
        if self._test_data is None:
            self._test_data = self._get_test_data()

        return [
            {
                'name': 'Абитуриенты факультета',
                'method': 'get_faculty_abiturients',
                'args': [self._test_data['faculty']]
            },
            {
                'name': 'Оценки студента',
                'method': 'get_abiturient_grades',
                'args': [
                    self._test_data['abiturient']['last_name'],
                    self._test_data['abiturient']['first_name']
                ]
            },
            {
                'name': 'Расписание студента по предмету',
                'method': 'get_abiturient_subject_schedule',
                'args': [
                    self._test_data['abiturient']['last_name'],
                    self._test_data['abiturient']['first_name'],
                    self._test_data['subject']
                ]
            },
            {
                'name': 'Расписание группы',
                'method': 'get_group_schedule',
                'args': [self._test_data['group']]
            },
            {
                'name': 'Рейтинг факультета',
                'method': 'get_faculty_rating',
                'args': [self._test_data['faculty']]
            },
            {
                'name': 'Средние оценки факультета',
                'method': 'get_faculty_avg_grades',
                'args': [self._test_data['faculty']]
            }
        ]

    def run_tests(self, size: int) -> None:
        """Запуск тестов для заданного размера базы"""
        queries = self._get_queries()

        for query in queries:
            avg_time = self.measure_time(
                query['method'],
                *query['args'],
                sort=self.sort,
                limit=self.limit
            )

            if query['name'] not in self.benchmark_results:
                self.benchmark_results[query['name']] = {}

            self.benchmark_results[query['name']][size] = avg_time

    def print_database_stats(self, size: int) -> None:
        """Вывод статистики базы данных"""
        with get_repository() as repo:
            print(f"📊 Тестирование на {size} записях:")
            print(f"   - Абитуриентов: {repo.abiturient.get_count()}")
            print(f"   - Факультетов: {repo.faculty.get_count()}")
            print(f"   - Групп: {repo.study_group.get_count()}")
            print(f"   - Предметов: {repo.subject.get_count()}")

    def generate_report(self) -> None:
        """Генерация отчета с таблицей и графиками"""
        self._print_table()
        self._plot_results()

    def _print_table(self) -> None:
        """Вывод сводной таблицы производительности"""
        print("\n📊 СВОДНАЯ ТАБЛИЦА ПРОИЗВОДИТЕЛЬНОСТИ (среднее время выполнения, мс)\n")

        header = f"{'ЗАПРОС':<40}"
        for size in self.test_sizes:
            header += f" | {f'{size} зап.':>12}"
        print(header)
        print("-" * 200)

        for query_name in self.benchmark_results:
            row = f"{query_name:<40}"

            for size in self.test_sizes:
                avg_time = self.benchmark_results[query_name][size]
                row += f" | {avg_time:>12.2f}"

            print(row)

    def run_benchmark(self) -> None:
        """Основной метод запуска всего бенчмарка"""
        for size in self.test_sizes:
            print(f"\n🔄 Подготовка БД с {size} записями...")
            self.prepare_db(size)
            self.print_database_stats(size)
            self.run_tests(size)

        self.generate_report()


def main():
    """Точка входа в программу"""
    benchmark = DatabaseBenchmark(
        test_sizes=[100, 1000, 10_000],
        sort=True,
        limit=5
    )
    benchmark.run_benchmark()


if __name__ == '__main__':
    main()