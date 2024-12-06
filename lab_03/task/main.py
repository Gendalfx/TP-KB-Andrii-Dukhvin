import sys
from student_list import StudentList
from file_manager import FileManager

def main():
    if len(sys.argv) < 2:
        print("No input file provided. Exiting...")
        sys.exit(1)

    file_name = sys.argv[1]

    file_manager = FileManager()

    # Завантажуємо дані з CSV
    students = file_manager.load_data_from_csv(file_name)

    # Створюємо об'єкт StudentList з уже завантаженими студентами
    student_list = StudentList(students)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                student_list.add_student()
                student_list.print_all_students()
            case "U" | "u":
                print("Existing element will be updated:")
                student_list.update_student()
                student_list.print_all_students()
            case "D" | "d":
                print("Element will be deleted:")
                student_list.delete_student()
                student_list.print_all_students()
            case "P" | "p":
                print("List will be printed:")
                student_list.print_all_students()
            case "X" | "x":
                print("Exiting program...")
                # Зберігаємо дані в CSV
                file_manager.save_data_to_csv(file_name, student_list.get_all_students())
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
