def makeLog(First_num, operation, Second_num, result):
    with open("topic_06/task_1/log/log.txt", "a") as f:                         #Відкриття файлу в режимі додавання
        f.write(f"{First_num=} {operation=} {Second_num=} {result=}\n")         #Запис даних у файл First_num=<значення> operation=<значення> Second_num=<значення> result=<значення>
