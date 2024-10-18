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
    while True:
        # Запит на введення числа або команди для завершення
        user_input = input("Введіть перше число: або 'q': ")
        if user_input.lower() == 'q':
            print("Програма завершена.")
            break
        
        try:
            num1 = float(user_input)
        except ValueError:
            print("Введіть перше число: або 'q': ")
            continue

        # Запит на введення другого числа
        user_input = input("Введіть друге число: або 'q': ")
        if user_input.lower() == 'q':
            print("Програма завершена.")
            break
        
        try:
            num2 = float(user_input)
        except ValueError:
            print("Введіть перше число: або 'q': ")
            continue

        # Запит на вибір операції
        operation = input("Оберіть операцію (+, -, *, /): ")
        if operation.lower() == 'q':
            print("Програма завершена.")
            break

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

# Виклик програми
calculator()
