# Функції для операцій
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        if a == 0 or b == 0:  
            raise ZeroDivisionError("Помилка: ділення на нуль!")  
        return a / b
    except ZeroDivisionError as e:
        print(e)  # Виводимо повідомлення про помилку
        
# Основна програма
def calculator():
    while True:
        # Запит на введення першого числа або команди для завершення
        try:
            user_input = input("Введіть перше число або 'q': ")
            if user_input.lower() == 'q':
                print("Програма завершена.")
                break  # Завершення програми при введенні 'q'
            num1 = float(user_input)
        except ValueError:
            print("Помилка: Введено нечислове значення. Спробуйте ще раз.")
            continue  # Продовжуємо запит

        # Запит на введення другого числа
        while True:  # Цикл для другого числа
            try:
                user_input = input("Введіть друге число або 'q': ")
                if user_input.lower() == 'q':
                    print("Програма завершена.")
                    return  # Завершення програми при введенні 'q'
                num2 = float(user_input)
                break  # Виходимо з циклу при коректному введенні
            except ValueError:
                print("Помилка: Введено нечислове значення. Спробуйте ще раз.")
                continue  # Повторюємо запит

        # Запит на вибір операції
        while True:
            operation = input("Оберіть операцію (+, -, *, /): ")
            if operation.lower() == 'q':
                print("Програма завершена.")
                return  # Завершення програми при введенні 'q'

            # Обробка операцій
            if operation == '+':
                print("Результат:", add(num1, num2))
                break
            elif operation == '-':
                print("Результат:", subtract(num1, num2))
                break
            elif operation == '*':
                print("Результат:", multiply(num1, num2))
                break
            elif operation == '/':
                result = divide(num1, num2)
                if result is not None:  # Якщо не було помилки
                    print("Результат:", result)
                    break  # Завершуємо цикл після виконання операції
            else:
                print("Невідома операція. Спробуйте ще раз.")
                continue  # Якщо операція неправильна, запитуємо ще раз

# Виклик програми
calculator()
