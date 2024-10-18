def find_insert_position(sorted_list, new_element):
    low = 0
    high = len(sorted_list)

    while low < high:
        mid = (low + high) // 2
        if sorted_list[mid] < new_element:
            low = mid + 1
        else:
            high = mid
            
    return low

# Введення відсортованого списку
sorted_list = [1, 2, 3, 4]

# Введення нового елемента
new_element = int(input("Введіть новий елемент для вставки: "))

# Знаходження позиції для вставки
position = find_insert_position(sorted_list, new_element)

# Вивід результату
print(f"Позиція для вставки {new_element} в список: {position}")

# Вставка нового елементу у список і виведення оновленого списку
sorted_list.insert(position, new_element)
print(f"Оновлений список: {sorted_list}")