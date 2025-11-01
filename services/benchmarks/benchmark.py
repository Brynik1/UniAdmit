from time import perf_counter

import matplotlib.pyplot as plt

from core import config
from database import db_manager
from database.queries import (
    get_faculty_students,
    get_student_grades,
    get_student_subject_schedule,
    get_group_schedule,
    get_faculty_rating,
    get_faculty_avg_grades,
    get_faculties_with_students,
    get_students_sample,
    get_groups_sample,
    get_subjects_sample
)
from services.seeding import seeder

# Конфигурация тестирования
# TEST_SIZES = [100, 5000, 10000, 50000, 100000, 500000, 1000000]
TEST_SIZES = [100, 1000, 2000]
ITERATIONS = 3

# Глобальная переменная для хранения результатов
benchmark_results = []


def prepare_database(size):
    """Подготовка базы данных с заданным количеством записей"""
    print(f"🔄 Подготовка БД с {size} записями...")

    db_manager.drop_tables()
    db_manager.create_tables()

    # Настройка конфигурации
    config.data.mode = 'bulk'
    config.data.student_count = size
    config.data.faculty_count = max(10, size // 100)
    config.data.school_count = max(10, size // 100)
    config.data.group_count = max(10, size // 50)
    config.data.stream_count = max(10, size // 50)
    config.data.subject_count = max(10, size // 100)
    config.data.batch_size = min(1000, size // 10)

    seeder.seed()

    return get_test_data()


def get_test_data():
    """Получает реальные данные из БД для использования в тестах"""
    test_data = {}

    with db_manager.get_session() as session:

        faculties = get_faculties_with_students(session)
        test_data['faculties'] = [f[0] for f in faculties[:5]] if faculties else ["Факультет компьютерных технологий"]

        students = get_students_sample(session)
        test_data['students'] = [{'last_name': s[0], 'first_name': s[1]} for s in students[:5]] if students else [
            {'last_name': 'Иванов', 'first_name': 'Алексей'}]

        groups = get_groups_sample(session)
        test_data['groups'] = [g[0] for g in groups[:5]] if groups else ["ПИ-101"]

        subjects = get_subjects_sample(session)
        test_data['subjects'] = [s[0] for s in subjects[:5]] if subjects else ["Математика"]

    return test_data


def measure_query_time(query_func, *args, iterations=ITERATIONS, **kwargs):
    """Измеряет время выполнения запроса"""
    times = []

    for _ in range(iterations):
        start_time = perf_counter()

        with db_manager.get_session() as session:
            query_func(*args, session, **kwargs)

        execution_time = (perf_counter() - start_time) * 1000  # мс
        times.append(execution_time)

    return sum(times) / iterations


def run_query_tests(size, test_data):
    """Запуск тестов для основных запросов"""
    queries = [
        {
            'name': 'Абитуриенты факультета',
            'func': get_faculty_students,
            'args': [test_data['faculties'][0]],
            'kwargs': {'limit': 5}
        },
        {
            'name': 'Оценки студента',
            'func': get_student_grades,
            'args': [
                test_data['students'][0]['last_name'],
                test_data['students'][0]['first_name']
            ],
            'kwargs': {'limit': 5}
        },
        {
            'name': 'Расписание студента по предмету',
            'func': get_student_subject_schedule,
            'args': [
                test_data['students'][0]['last_name'],
                test_data['students'][0]['first_name'],
                test_data['subjects'][0]
            ],
            'kwargs': {'limit': 5}
        },
        {
            'name': 'Расписание группы',
            'func': get_group_schedule,
            'args': [test_data['groups'][0]],
            'kwargs': {'limit': 5}
        },
        {
            'name': 'Рейтинг факультета',
            'func': get_faculty_rating,
            'args': [test_data['faculties'][0]],
            'kwargs': {'limit': 5}
        },
        {
            'name': 'Средние оценки факультета',
            'func': get_faculty_avg_grades,
            'args': [test_data['faculties'][0]],
            'kwargs': {'limit': 5}
        }
    ]

    for query in queries:
        try:
            result = measure_query_time(query['func'], *query['args'], **query['kwargs'])

            benchmark_results.append({
                'size': size,
                'query': query['name'],
                'result': result
            })

            print(f"   ✅ {query['name']}: {result:.2f} мс")

        except Exception as e:
            print(f"   ❌ Ошибка в запросе '{query['name']}': {e}")


def generate_report():
    """Генерация отчета по результатам бенчмарка"""

    # Выводим таблицу
    print("\n📊 СВОДНАЯ ТАБЛИЦА ПРОИЗВОДИТЕЛЬНОСТИ (среднее время выполнения, мс)\n")
    print("=" * 85)

    # Заголовок таблицы с выравниванием
    header = f"{'ЗАПРОС':<40}"
    for size in TEST_SIZES:
        header += f" | {f'{size} зап.':>12}"
    print(header)
    print("-" * 200)

    # Получаем уникальные запросы и сортируем их
    unique_queries = sorted(set(r['query'] for r in benchmark_results))

    for query in unique_queries:
        row = f"{query:<40}"

        for size in TEST_SIZES:
            # Ищем результат для этого запроса и размера
            result = next((r for r in benchmark_results
                           if r['size'] == size and r['query'] == query), None)

            if result:
                row += f" | {result['result']:>12.2f}"
            else:
                row += f" | {'N/A':>12}"

        print(row)


def run_benchmarks():
    """Запуск всех бенчмарков для разных размеров данных"""
    print("🚀 ЗАПУСК БЕНЧМАРК-ТЕСТОВ")
    print("=" * 50)

    for size in TEST_SIZES:
        print(f"\n📊 ТЕСТИРОВАНИЕ НА {size} ЗАПИСЯХ")

        # Подготавливаем БД и получаем тестовые данные
        test_data = prepare_database(size)

        # Запускаем тесты для каждого запроса
        run_query_tests(size, test_data)


def plot_performance_charts():
    """Строит графики производительности запросов"""
    plt.figure(figsize=(14, 8))

    unique_queries = sorted(set(r['query'] for r in benchmark_results))
    sizes = sorted(set(r['size'] for r in benchmark_results))

    # График: Зависимость времени от размера БД для каждого запроса
    for query in unique_queries:
        times = []
        valid_sizes = []
        for size in sizes:
            result = next((r for r in benchmark_results
                           if r['size'] == size and r['query'] == query), None)
            if result:
                times.append(result['result'])
                valid_sizes.append(size)

        if times:
            plt.plot(valid_sizes, times, marker='o', linewidth=2, markersize=6,
                     label=query[:25] + '...' if len(query) > 25 else query)

    plt.xlabel('Количество записей (логарифмическая шкала)')
    plt.ylabel('Время выполнения (мс, логарифмическая шкала)')
    plt.title('Зависимость времени выполнения запросов от размера базы данных')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.xscale('log')
    plt.yscale('log')

    plt.tight_layout()
    plt.show()



def main():
    """Основная функция для запуска бенчмарка"""

    run_benchmarks()
    generate_report()
    plot_performance_charts()


if __name__ == "__main__":
    main()