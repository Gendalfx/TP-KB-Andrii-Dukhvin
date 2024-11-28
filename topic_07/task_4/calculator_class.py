from functions import Functions
from operations import Operations
from log import Logger

class Calculator:
    def __init__(self):
        self.functions = Functions()
        self.operations = Operations()
        self.logger = Logger()

    def run(self):
        while True:
            num1 = self.operations.get_first_number()
            if num1 is None:
                break

            num2 = self.operations.get_second_number()
            if num2 is None:
                break

            while True:
                operation = self.operations.get_operation()
                if operation is None:
                    return

                if operation not in ('+', '-', '*', '/'):
                    error_message = f"Unknown operation: {operation}. Please try again."
                    print(error_message)
                    self.logger.make_log(num1, operation, num2, error_message)
                    continue

                match operation:
                    case '+':
                        result = self.functions.add(num1, num2)
                    case '-':
                        result = self.functions.subtract(num1, num2)
                    case '*':
                        result = self.functions.multiply(num1, num2)
                    case '/':
                        result = self.functions.divide(num1, num2)
                        if result is None:
                            self.logger.make_log(num1, operation, num2, "Error: division by zero!")
                            continue

                print("Result:", result)
                self.logger.make_log(num1, operation, num2, result)
                break
