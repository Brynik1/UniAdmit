from time import perf_counter
import matplotlib.pyplot as plt

from database import db_manager
from services.data import seeder
from services.context_db import get_repository
from core import config


TEST_SIZES = [100, 5000, 10000]
SORT = False
LIMIT = 5

benchmark_results = {}


def prepare_db(size):
    print(f"🔄 Подготовка БД с {size} записями...")

    db_manager.drop_tables()
    db_manager.create_tables()

    config.data.mode = 'bulk'
    config.data.student_count = size
    config.data.faculty_count = max(10, size // 100)
    config.data.school_count = max(10, size // 100)
    config.data.group_count = max(10, size // 50)
    config.data.stream_count = max(10, size // 50)
    config.data.subject_count = max(10, size // 100)
    config.data.batch_size = min(1000, size // 10)

    seeder.seed()


def get_test_data():
    test_data = {}

    with get_repository() as repo:
        faculty_sample = repo.faculty.get_sample()
        test_data['faculty'] = faculty_sample[0]

        student_sample = repo.abiturient.get_sample()
        test_data['student'] = {'last_name': student_sample[0], 'first_name': student_sample[1]}

        group_sample = repo.study_group.get_sample()
        test_data['group'] = group_sample[0]

        subject_sample = repo.subject.get_sample()
        test_data['subject'] = subject_sample[0]

    return test_data


def measure_time(repo_method, *args, **kwargs):
    sum_times = 0

    for _ in range(5):
        start_time = perf_counter()

        with get_repository() as repo:
            method = getattr(repo, repo_method)
            method(*args, **kwargs)

        sum_times += (perf_counter() - start_time) * 1000

    return sum_times / 5


def run_tests(size):
    test_data = get_test_data()
    queries = [
        {
            'name': 'Абитуриенты факультета',
            'method': 'get_faculty_students',
            'args': [test_data['faculty']]
        },
        {
            'name': 'Оценки студента',
            'method': 'get_student_grades',
            'args': [
                test_data['student']['last_name'],
                test_data['student']['first_name']
            ]
        },
        {
            'name': 'Расписание студента по предмету',
            'method': 'get_student_subject_schedule',
            'args': [
                test_data['student']['last_name'],
                test_data['student']['first_name'],
                test_data['subject']
            ]
        },
        {
            'name': 'Расписание группы',
            'method': 'get_group_schedule',
            'args': [test_data['group']]
        },
        {
            'name': 'Рейтинг факультета',
            'method': 'get_faculty_rating',
            'args': [test_data['faculty']]
        },
        {
            'name': 'Средние оценки факультета',
            'method': 'get_faculty_avg_grades',
            'args': [test_data['faculty']]
        }
    ]

    for query in queries:
        avg_time = measure_time(query['method'], *query['args'], sort=SORT, limit=LIMIT)

        if query['name'] not in benchmark_results:
            benchmark_results[query['name']] = {}

        benchmark_results[query['name']][size] = avg_time


def report():

    print("\n📊 СВОДНАЯ ТАБЛИЦА ПРОИЗВОДИТЕЛЬНОСТИ (среднее время выполнения, мс)\n")

    header = f"{'ЗАПРОС':<40}"
    for size in TEST_SIZES:
        header += f" | {f'{size} зап.':>12}"
    print(header)
    print("-" * 200)

    for query in benchmark_results.keys():
        row = f"{query:<40}"

        for size in TEST_SIZES:
            avg_time = benchmark_results[query][size]
            row += f" | {avg_time:>12.2f}"

        print(row)

    # Построение графиков
    plt.figure(figsize=(12, 8))

    for query_name in benchmark_results:
        sizes = []
        times = []
        for size in TEST_SIZES:
            sizes.append(size)
            times.append(benchmark_results[query_name][size])
        plt.plot(sizes, times, marker='o', label=query_name)

    plt.xlabel('Количество записей')
    plt.ylabel('Время выполнения (мс)')
    plt.title('Зависимость времени выполнения от количества записей')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    for size in TEST_SIZES:
        print(f"\n📊 ТЕСТИРОВАНИЕ НА {size} ЗАПИСЯХ")

        prepare_db(size)
        run_tests(size)

    report()

