class Functions:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("Error: Division by zero!")
            return a / b
        except ZeroDivisionError as e:
            print(e)
            return None
