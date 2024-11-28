class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

# Створюємо список об'єктів класу Student
students = [
    Student("Alice", 21),
    Student("Bob", 19),
    Student("Charlie", 22),
    Student("David", 20)
]

# Сортуємо список за ім'ям (name) використовуючи функцію sorted з лямбда-функцією
sorted_by_name = sorted(students, key=lambda student: student.name)

# Сортуємо список за віком (age) використовуючи функцію sorted з лямбда-функцією
sorted_by_age = sorted(students, key=lambda student: student.age)

# Виводимо відсортовані елементи списку за ім'ям
print("Sorted by name:")
for student in sorted_by_name:
    print(student)

# Виводимо відсортовані елементи списку за віком
print("\nSorted by age:")
for student in sorted_by_age:
    print(student)

