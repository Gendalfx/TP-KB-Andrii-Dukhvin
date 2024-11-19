def get_first_number():
    while True:
        try:
            user_input = input("Введіть перше число або 'q': ")
            if user_input.lower() == 'q':
                print("Програма завершена.")
                return None
            return float(user_input)
        except ValueError:
            print("Помилка: Введено нечислове значення. Спробуйте ще раз.")

def get_second_number():
    while True:
        try:
            user_input = input("Введіть друге число або 'q': ")
            if user_input.lower() == 'q':
                print("Програма завершена.")
                return None
            return float(user_input)
        except ValueError:
            print("Помилка: Введено нечислове значення. Спробуйте ще раз.")

def get_operation():
    while True:
        operation = input("Оберіть операцію (+, -, *, /): ")
        if operation.lower() == 'q':
            print("Програма завершена.")
            return None
        if operation in ('+', '-', '*', '/'):
            return operation
        else:
            print("Невідома операція. Спробуйте ще раз.")
