from database import db_manager
from database.queries import (
    get_faculty_students, get_student_grades, get_student_subject_schedule,
    get_group_schedule, get_faculty_rating, get_faculty_avg_grades,
    create_school, get_schools, update_school, delete_school
)


def execute_all_queries():
    """Выполняет все требуемые запросы к базе данных в рамках одной сессии"""

    with db_manager.get_session() as session:

        print("\nПоследние 3 строки таблицы школ:")
        all_schools = get_schools(session)
        last_3_schools = all_schools[-3:] if len(all_schools) >= 3 else all_schools
        for school in last_3_schools:
            print(f"   - {school.name}: {school.address}")

        print("\n1) Выполнение запроса на добавление новой школы")
        new_school_name = "Новая школа №5"
        new_school_address = "Новый адрес"
        create_school(new_school_name, new_school_address, session)

        print("Последние 3 строки таблицы школ:")
        all_schools = get_schools(session)
        last_3_schools = all_schools[-3:] if len(all_schools) >= 3 else all_schools
        for school in last_3_schools:
            print(f"   - {school.name}: {school.address}")


        print("\n2) Выполнение запроса на обновление адреса новой школы")
        updated_address = "Обновленный адрес"
        update_school(
            session=session,
            name=new_school_name,
            address=new_school_address,
            new_address=updated_address
        )
        print("Последние 3 строки таблицы школ:")
        all_schools = get_schools(session)
        last_3_schools = all_schools[-3:] if len(all_schools) >= 3 else all_schools
        for school in last_3_schools:
            print(f"   - {school.name}: {school.address}")


        print("\n3) Выполнение запроса на удаление новой школы")
        delete_school(
            session=session,
            name=new_school_name,
            address=updated_address
        )

        print("Последние 3 строки таблицы школ:")
        all_schools = get_schools(session)
        last_3_schools = all_schools[-3:] if len(all_schools) >= 3 else all_schools
        for school in last_3_schools:
            print(f"   - {school.name}: {school.address}")


        print("\n4) Абитуриенты факультета компьютерных технологий:")
        faculty_name = 'Факультет компьютерных технологий'
        faculty_students = get_faculty_students(faculty_name, session)
        for student in faculty_students:
            print(f"   - {student.Фамилия} {student.Имя} {student.Отчество or ''}: "
                  f"{student.Кафедра} ({'Зачислен' if student.Зачислен == 'Да' else 'Не зачислен'})")

        print("\n5) Оценки абитуриента Иванов Алексей:")
        student_grades = get_student_grades('Иванов', 'Алексей', session)
        for grade in student_grades:
            print(f"   - {grade.Предмет}: {grade.Оценка} баллов "
                  f"({grade.Дата_экзамена}) {'[Апелляция]' if grade.Апелляция == 'Да' else ''}")

        print("\n6) Расписание по математике для Иванова Алексея:")
        student_schedule = get_student_subject_schedule('Иванов', 'Алексей', 'Математика', session)
        for schedule in student_schedule:
            print(f"   - {schedule.Дата}: {schedule.Тип} по {schedule.Предмет} "
                  f"в {schedule.Аудитория}")

        print("\n7) Расписание экзаменов для группы ПИ-101:")
        group_schedule = get_group_schedule('ПИ-101', session)
        for schedule in group_schedule:
            print(f"   - {schedule.Дата}: {schedule.Тип} по {schedule.Предмет} "
                  f"в {schedule.Аудитория}")

        print("\n8) Рейтинг абитуриентов факультета компьютерных технологий:")
        faculty_rating = get_faculty_rating('Факультет компьютерных технологий', session)
        for i, student in enumerate(faculty_rating, 1):
            print(f"   - {i}. {student.Фамилия} {student.Имя}: {student.Сумма_баллов} баллов "
                  f"({student.Медаль} медаль)")

        print("\n9) Средний балл по предметам на факультете компьютерных технологий:")
        faculty_avg_grades = get_faculty_avg_grades('Факультет компьютерных технологий', session)
        for subject in faculty_avg_grades:
            print(f"   - {subject.Предмет}: {subject.Средний_балл}")
