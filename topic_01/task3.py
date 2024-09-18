def find_discriminant(a, b, c):
    # Обчислюємо дискримінант
    discriminant = b**2 - 4*a*c
    return discriminant

# Приклад використання
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

# Виклик функції та виведення результату
D = find_discriminant(a, b, c)
print(f"Дискримінант: {D}")
