from services.context_db import get_repository


def execute_all_queries():
    """Выполняет все требуемые запросы к базе данных в рамках одной сессии"""

    with get_repository() as repo:

        print("\nПоследние 3 строки таблицы школ:")
        last_3 = repo.school.get_sample(limit=3)
        for school in last_3[::-1]:
            print(f"   - {school.school_name}: {school.address}")

        print("\n1) Выполнение запроса на добавление новой школы")
        new_school_name = "Новая школа №5"
        new_school_address = "Новый адрес"
        repo.school.create(
            name=new_school_name,
            address=new_school_address
        )

        print("Последние 3 записи таблицы школ:")
        last_3 = repo.school.get_sample(limit=3)
        for school in last_3[::-1]:
            print(f"   - {school.school_name}: {school.address}")


        print("\n2) Выполнение запроса на обновление адреса новой школы")
        updated_address = "Обновленный адрес"
        repo.school.update(
            name=new_school_name,
            address=new_school_address,
            new_address=updated_address
        )
        print("Последние 3 записи таблицы школ:")
        last_3 = repo.school.get_sample(limit=3)
        for school in last_3[::-1]:
            print(f"   - {school.school_name}: {school.address}")


        print("\n3) Выполнение запроса на удаление новой школы")
        repo.school.delete(name=new_school_name, address=updated_address)

        print("Последние 3 записи таблицы школ:")
        last_3 = repo.school.get_sample(limit=3)
        for school in last_3:
            print(f"   - {school.school_name}: {school.address}")


        print("\n4) Абитуриенты факультета компьютерных технологий:")
        faculty_name = 'Факультет компьютерных технологий'
        faculty_abiturients = repo.get_faculty_abiturients(faculty_name)
        for abiturient in faculty_abiturients:
            print(f"   - {abiturient.last_name} {abiturient.first_name} {abiturient.patronymic or ''}: "
                  f"{abiturient.department_name} ({'Зачислен' if abiturient.Зачислен == 'Да' else 'Не зачислен'})")

        print("\n5) Оценки абитуриента Иванов Алексей:")
        abiturient_grades = repo.get_abiturient_grades('Иванов', 'Алексей')
        for grade in abiturient_grades:
            print(f"   - {grade.subject_name}: {grade.grade} баллов "
                  f"({grade.exam_date}) {'[Апелляция]' if grade.Апелляция == 'Да' else ''}")

        print("\n6) Расписание по математике для Иванова Алексея:")
        abiturient_schedule = repo.get_abiturient_subject_schedule('Иванов', 'Алексей', 'Математика')
        for schedule in abiturient_schedule:
            print(f"   - {schedule.schedule_date}: {schedule.Тип} по {schedule.subject_name} "
                  f"в {schedule.classroom}")

        print("\n7) Расписание экзаменов для группы ПИ-101:")
        group_schedule = repo.get_group_schedule('ПИ-101')
        for schedule in group_schedule:
            print(f"   - {schedule.schedule_date}: {schedule.Тип} по {schedule.subject_name} "
                  f"в {schedule.classroom}")

        print("\n8) Рейтинг абитуриентов факультета компьютерных технологий:")
        faculty_rating = repo.get_faculty_rating('Факультет компьютерных технологий', sort=True)
        for i, abiturient in enumerate(faculty_rating, 1):
            print(f"   - {i}. {abiturient.last_name} {abiturient.first_name}: {abiturient.Сумма_баллов} баллов "
                  f"({abiturient.Медаль} медаль)")

        print("\n9) Средний балл по предметам на факультете компьютерных технологий:")
        faculty_avg_grades = repo.get_faculty_avg_grades('Факультет компьютерных технологий')
        for subject in faculty_avg_grades:
            print(f"   - {subject.subject_name}: {subject.Средний_балл}")

        print()