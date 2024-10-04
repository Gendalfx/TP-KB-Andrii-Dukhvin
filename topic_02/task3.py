# Функції для операцій
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    return "Помилка: ділення на нуль!"

# Основна програма
def calculator():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    operation = input("Оберіть операцію (+, -, *, /): ")

    match operation:
        case '+':
            print("Результат:", add(num1, num2))
        case '-':
            print("Результат:", subtract(num1, num2))
        case '*':
            print("Результат:", multiply(num1, num2))
        case '/':
            print("Результат:", divide(num1, num2))
        case _:
            print("Невідома операція")

calculator()
