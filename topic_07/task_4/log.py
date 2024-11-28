from datetime import datetime

class Logger:
    @staticmethod
    def make_log(first_num, operation, second_num, result):
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("topic_07/task_4/log.txt", "a") as f:
            f.write(f"{current_time} - First_num={first_num} operation='{operation}' Second_num={second_num} result={result}\n")
