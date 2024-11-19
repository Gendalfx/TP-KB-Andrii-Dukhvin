students = [
    {"name": "Alice", "score": 10},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 95},
    {"name": "David", "score": 22},
    {"name": "Eva", "score": 18},
    {"name": "Frank", "score": 19},
    {"name": "Grace", "score": 14},
    {"name": "Hannah", "score": 92},
    {"name": "Ian", "score": 4},
    {"name": "Jack", "score": 14},
    {"name": "Karen", "score": 14},
    {"name": "Leo", "score": 100},
    {"name": "Mia", "score": 7},
    {"name": "Nina", "score": 79},
    {"name": "Oscar", "score": 1},
]

# Сортування за ім'ям
sorted_by_name = sorted(students, key=lambda student: student["name"])
# Сортування за балом
sorted_by_score = sorted(students, key=lambda student: student["score"])

print("Сортування за ім'ям в алфавітному порядку: ", sorted_by_name)
print("Сортування за найвищим балом: ", sorted_by_score)