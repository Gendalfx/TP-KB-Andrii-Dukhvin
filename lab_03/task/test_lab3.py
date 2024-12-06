import pytest
from student import Student
from student_list import StudentList


# Тест для додавання студента
def test_add_student(monkeypatch):
    # Моделюємо введення користувача для створення студента
    inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    student_list = StudentList()
    student_list.add_student()

    # Перевірка, що студент був доданий у список
    assert len(student_list.students) == 1
    assert student_list.students[0].name == "Alice"
    assert student_list.students[0].phone == "0631112222"
    assert student_list.students[0].email == "alice@example.com"
    assert student_list.students[0].address == "321 Cedar St"


# Тест для видалення студента
def test_delete_student(monkeypatch):
    # Моделюємо введення користувача для створення студента
    inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St", "Alice"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))


    student_list = StudentList()
    student_list.add_student()

    # Перевірка, що студент доданий
    assert len(student_list.students) == 1

    # Видалення студента
    student_list.delete_student()

    # Перевірка, що студент був видалений
    assert len(student_list.students) == 0


# Тест для оновлення студента
def test_update_student(monkeypatch):
    # Моделюємо введення користувача для створення студента та оновлення його даних
    add_inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St"])
    update_inputs = iter(["Alice", "123", "new_email@example.com", "New Address"])

    # Підставляємо введення для додавання студента
    monkeypatch.setattr('builtins.input', lambda _: next(add_inputs))

    student_list = StudentList()
    student_list.add_student()

    # Перевірка, що студент був доданий
    assert len(student_list.students) == 1

    # Подставляємо введення для оновлення студента
    monkeypatch.setattr('builtins.input', lambda _: next(update_inputs))
    # Оновлення студента
    student_list.update_student()

     # Перевірка, що студент був оновлений
    for student in student_list.students:
        if student.name == "Alice":  # Ищем студента с исходным именем
            assert student.phone == "123"
            assert student.email == "new_email@example.com"
            assert student.address == "New Address"
            return  
    assert False, "Студент Alice не знайдений"
    


def test_print_all_students(monkeypatch, capsys):
    # Моделюємо введення користувача для створення студента
    add_inputs = iter(["Alice", "0631112222", "alice@example.com", "321 Cedar St"])
    monkeypatch.setattr('builtins.input', lambda _: next(add_inputs))

    # Створення екземпляра списку студентів
    student_list = StudentList()

    # Додавання студента
    student_list.add_student()

    # Перевірка, що студент був доданий
    assert len(student_list.students) == 1

    # Виклик методу для виведення всіх студентів
    student_list.print_all_students()

    # Захоплення виходу
    captured = capsys.readouterr()

    # Перевірка, що вивід містить інформацію про студента
    assert "Student name is Alice" in captured.out
    assert "Phone is 0631112222" in captured.out
    assert "Email is alice@example.com" in captured.out
    assert "Address is 321 Cedar St" in captured.out


