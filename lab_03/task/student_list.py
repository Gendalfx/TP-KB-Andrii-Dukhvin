from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Please enter student name: ")
        phone = input("Please enter student phone: ")
        email = input("Please enter student email: ")
        address = input("Please enter student address: ")
        new_student = Student(name, phone, email, address)
        insert_position = 0
        for student in self.students:
            if name > student.name:
                insert_position += 1
            else:
                break
        self.students.insert(insert_position, new_student)
        print(f"Student {name} has been added.")

    def delete_student(self):
        name = input("Please enter name to be deleted: ")
        delete_position = -1
        for index, student in enumerate(self.students):
            if student.name == name:
                delete_position = index
                break
        if delete_position == -1:
            print(f"Student {name} not found.")
        else:
            del self.students[delete_position]
            print(f"Student {name} has been deleted.")

    def update_student(self):
        name = input("Please enter name to be updated: ")
        student_found = False
        for student in self.students:
            if student.name == name:
                student_found = True
                phone = input(f"Enter new phone (current: {student.phone}): ")
                email = input(f"Enter new email (current: {student.email}): ")
                address = input(f"Enter new address (current: {student.address}): ")
                student.phone = phone
                student.email = email
                student.address = address
                break
        if not student_found:
            print(f"Student {name} not found.")
        else:
            self.students.sort(key=lambda x: x.name)
            print(f"Student {name} has been updated.")

    def print_all_students(self):
        for student in self.students:
            print(f"Student name is {student.name}, Phone is {student.phone}, Email is {student.email}, Address is {student.address}")

    def get_all_students(self):
        return self.students
