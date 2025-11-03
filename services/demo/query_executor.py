from database import db_manager, MainRepository
from services.dependencies import get_main_repository


def execute_all_queries():
    """Выполняет все требуемые запросы к базе данных в рамках одной сессии"""

    with get_main_repository() as repo:

        print("\nПоследние 3 строки таблицы школ:")
        last_3 = repo.get_schools(limit=3)
        for school in last_3[::-1]:
            print(f"   - {school.name}: {school.address}")

        print("\n1) Выполнение запроса на добавление новой школы")
        new_school_name = "Новая школа №5"
        new_school_address = "Новый адрес"
        repo.school.create(new_school_name, new_school_address)

        print("Последние 3 записи таблицы школ:")
        last_3 = repo.get_schools(limit=3)
        for school in last_3[::-1]:
            print(f"   - {school.name}: {school.address}")


        print("\n2) Выполнение запроса на обновление адреса новой школы")
        updated_address = "Обновленный адрес"
        repo.school.update(
            name=new_school_name,
            address=new_school_address,
            new_address=updated_address
        )
        print("Последние 3 записи таблицы школ:")
        last_3 = repo.get_schools(limit=3)
        for school in last_3[::-1]:
            print(f"   - {school.name}: {school.address}")


        print("\n3) Выполнение запроса на удаление новой школы")
        repo.school.delete(name=new_school_name, address=updated_address)

        print("Последние 3 записи таблицы школ:")
        last_3 = repo.get_schools(limit=3)
        for school in last_3:
            print(f"   - {school.name}: {school.address}")


        print("\n4) Абитуриенты факультета компьютерных технологий:")
        faculty_name = 'Факультет компьютерных технологий'
        faculty_students = repo.get_faculty_students(faculty_name)
        for student in faculty_students:
            print(f"   - {student.Фамилия} {student.Имя} {student.Отчество or ''}: "
                  f"{student.Кафедра} ({'Зачислен' if student.Зачислен == 'Да' else 'Не зачислен'})")

        print("\n5) Оценки абитуриента Иванов Алексей:")
        student_grades = repo.get_student_grades('Иванов', 'Алексей')
        for grade in student_grades:
            print(f"   - {grade.Предмет}: {grade.Оценка} баллов "
                  f"({grade.Дата_экзамена}) {'[Апелляция]' if grade.Апелляция == 'Да' else ''}")

        print("\n6) Расписание по математике для Иванова Алексея:")
        student_schedule = repo.get_student_subject_schedule('Иванов', 'Алексей', 'Математика')
        for schedule in student_schedule:
            print(f"   - {schedule.Дата}: {schedule.Тип} по {schedule.Предмет} "
                  f"в {schedule.Аудитория}")

        print("\n7) Расписание экзаменов для группы ПИ-101:")
        group_schedule = repo.get_group_schedule('ПИ-101')
        for schedule in group_schedule:
            print(f"   - {schedule.Дата}: {schedule.Тип} по {schedule.Предмет} "
                  f"в {schedule.Аудитория}")

        print("\n8) Рейтинг абитуриентов факультета компьютерных технологий:")
        faculty_rating = repo.get_faculty_rating('Факультет компьютерных технологий')
        for i, student in enumerate(faculty_rating, 1):
            print(f"   - {i}. {student.Фамилия} {student.Имя}: {student.Сумма_баллов} баллов "
                  f"({student.Медаль} медаль)")

        print("\n9) Средний балл по предметам на факультете компьютерных технологий:")
        faculty_avg_grades = repo.get_faculty_avg_grades('Факультет компьютерных технологий')
        for subject in faculty_avg_grades:
            print(f"   - {subject.Предмет}: {subject.Средний_балл}")

        print()
