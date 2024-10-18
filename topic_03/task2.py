def test_list_functions():
    # Початковий список
    my_list = [1, 3, 2, 4]
    print("Початковий список:", my_list)

    # 1. append()
    my_list.append(5)
    print("Після append(5):", my_list)

    # 2. extend()
    my_list.extend([6, 7])
    print("Після extend([6, 7]):", my_list)

    # 3. insert(index, value)
    my_list.insert(0, 0)  # Вставка 0 на початок списку
    print("Після insert(0, 0):", my_list)

    # 4. remove(value)
    my_list.remove(3)  # Видалення значення 3
    print("Після remove(3):", my_list)

    # 5. clear()
    my_list.clear()
    print("Після clear():", my_list)

    # Повернемо список для подальшого тестування
    my_list = [3, 1, 4, 2]

    # 6. sort()
    my_list.sort()
    print("Після sort():", my_list)

    # 7. reverse()
    my_list.reverse()
    print("Після reverse():", my_list)

    # 8. copy()
    copied_list = my_list.copy()
    print("Скопійований список:", copied_list)

# Виклик функції тестування
test_list_functions()
