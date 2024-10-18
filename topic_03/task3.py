def test_dict_functions():
    # Початковий словник
    my_dict = {
        "name": "Andrii",
        "age": 25,
        "city": "Chernihiv"
    }
    print("Початковий словник:", my_dict)

    # 1. update()
    my_dict.update({
        "age": 26, "country": "Ukraine"
    })  # Оновлюємо вік та додаємо країну
    print("Після update:", my_dict)

    # 2. del
    del my_dict["city"]  # Видаляємо ключ "city"
    print("Після del: ", my_dict)

    # 3. clear()
    my_dict.clear()  # Очищаємо словник
    print("Після clear: ", my_dict)

    print("Повернемо словник для подальшого тестування")
    # Повернемо словник для подальшого тестування
    my_dict = {
        "name": "Andrii",
        "age": 25,
        "city": "Chernihiv"
    }

    # 4. keys()
    keys = my_dict.keys()  # Отримуємо ключі словника
    print("Ключі словника: ", list(keys))

    # 5. values()
    values = my_dict.values()  # Отримуємо значення словника
    print("Значення словника: ", list(values))

    # 6. items()
    items = my_dict.items()  # Отримуємо пари (ключ, значення)
    print("Пари (ключ, значення) словника: ", list(items))

# Виклик функції тестування
test_dict_functions()
