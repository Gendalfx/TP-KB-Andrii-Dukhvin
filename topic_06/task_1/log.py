from datetime import datetime

def makeLog(First_num, operation, Second_num, result):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Отримуємо поточну дату і час
    with open("topic_06/task_1/log/log.txt", "a") as f:  # Відкриття файлу в режимі додавання
        f.write(f"{current_time} - First_num={First_num} operation='{operation}' Second_num={Second_num} result={result}\n")  # Запис даних у файл з датою
