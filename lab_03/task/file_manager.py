import csv
from student import Student

class FileManager:
    def __init__(self):
        # Можна додати ініціалізацію, якщо необхідно
        pass

    def load_data_from_csv(self, file_name):
        try:
            with open(file_name, mode='r') as file:
                reader = csv.DictReader(file)
                students = [Student(row['name'], row['phone'], row['email'], row['address']) for row in reader]
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty list.")
            students = []
        return students

    def save_data_to_csv(self, file_name, students):
        with open(file_name, mode='w', newline='') as file:
            fieldnames = ["name", "phone", "email", "address"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                writer.writerow({"name": student.name, "phone": student.phone, "email": student.email, "address": student.address})
