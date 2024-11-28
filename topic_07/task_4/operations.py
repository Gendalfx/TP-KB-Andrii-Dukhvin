class Operations:
    @staticmethod
    def get_first_number():
        while True:
            try:
                user_input = input("Введіть перше число або 'q' для виходу: ")
                if user_input.lower() == 'q':
                    print("Програму завершено.")
                    return None
                return float(user_input)
            except ValueError:
                print("Помилка: Введено нечислове значення. Спробуйте ще раз.")

    @staticmethod
    def get_second_number():
        while True:
            try:
                user_input = input("Введіть друге число або 'q' для виходу: ")
                if user_input.lower() == 'q':
                    print("Програму завершено.")
                    return None
                return float(user_input)
            except ValueError:
                print("Помилка: Введено нечислове значення. Спробуйте ще раз.")

    @staticmethod
    def get_operation():
        while True:
            operation = input("Оберіть операцію (+, -, *, /) або 'q' для виходу: ")
            if operation.lower() == 'q':
                print("Програму завершено.")
                return None
            if operation in ('+', '-', '*', '/'):
                return operation
            else:
                print(f"Невідома операція: {operation}. Спробуйте ще раз.")
