class Person:
    def __init__(self, name, age):        #Він використовується для ініціалізації атрибутів класу
        self.name = name
        self.age = age

    def __str__(self):                   #Він має повертати рядок, який буде використовуватися як текстове представлення об'єкта
        return f"Person(name={self.name}, age={self.age})"

# Створюємо новий екземпляр класу Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)


print(person1.name)  # Виведе name
print(person1.age)   # Виведе age
print(person2) 
