def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Помилка: ділення на нуль!")
        return a / b
    except ZeroDivisionError as e:
        print(e)  # Виводимо повідомлення про помилку
        return None
