from functions import add, subtract, multiply, divide
from operations import get_first_number, get_second_number, get_operation
from log import makeLog

def calculator():
    while True:
        # Запит на введення першого числа або команди для завершення
        num1 = get_first_number()
        if num1 is None:
            break

        # Запит на введення другого числа або команди для завершення
        num2 = get_second_number()
        if num2 is None:
            break

        # Запит на вибір операції
        while True:
            operation = get_operation()
            if operation is None:
                return  # Завершення програми

            if operation not in ('+', '-', '*', '/'):
                error_message = f"Unknown operation: {operation}. Please try again."
                print(error_message)
                makeLog(num1, operation, num2, error_message)  # Логування помилки
                continue  # Запитуємо операцію знову

            # Обробка операцій за допомогою match-case
            match operation:
                case '+':
                    result = add(num1, num2)
                    print("Result:", result)
                    makeLog(num1, operation, num2, result)  # Логування дії
                    break
                case '-':
                    result = subtract(num1, num2)
                    print("Result:", result)
                    makeLog(num1, operation, num2, result)  # Логування дії
                    break
                case '*':
                    result = multiply(num1, num2)
                    print("Result:", result)
                    makeLog(num1, operation, num2, result)  # Логування дії
                    break
                case '/':
                    result = divide(num1, num2)
                    if result is not None:  # Якщо ділення на нуль не відбулося
                        print("Result:", result)
                        makeLog(num1, operation, num2, result)  # Логування дії
                        break
                    else:
                        makeLog(num1, operation, num2, "Error: division by zero!")  # Логування помилки
                        continue  # Запитуємо операцію знову

calculator()
