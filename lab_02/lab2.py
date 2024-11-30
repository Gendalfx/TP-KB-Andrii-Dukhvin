import csv
import sys

# Завантаження даних з CSV файлу
def load_data_from_csv(file_name):
    students = []
    try:
        with open(file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print(f"File {file_name} not found. Starting with an empty list.")
    return students

# Збереження даних у CSV файл
def save_data_to_csv(file_name, students):
    with open(file_name, mode='w', newline='') as file:
        fieldnames = ["name", "phone", "email", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

# Завантаження даних при запуску програми
if len(sys.argv) < 2:
    print("No input file provided. Exiting...")
    sys.exit(1)

file_name = sys.argv[1]
students_list = load_data_from_csv(file_name)

# Функції для роботи з довідником
def printAllList(students):
    for elem in students:
        strForPrint = f"Student name is {elem['name']}, Phone is {elem['phone']}, Email is {elem['email']}, Address is {elem['address']}"
        print(strForPrint)

def addNewElement(students):
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")
    newItem = {"name": name, "phone": phone, "email": email, "address": address}

    insertPosition = 0
    for item in students:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added")

def deleteElement(students):
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in students:
        if name == item["name"]:
            deletePosition = students.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print(f"Delete position {deletePosition}")
        del students[deletePosition]

def updateElement(students):
    name = input("Please enter name to be updated: ")
    studentFound = False
    for item in students:
        if item["name"] == name:
            studentFound = True
            newPhone = input(f"Enter new phone (current: {item['phone']}): ")
            newEmail = input(f"Enter new email (current: {item['email']}): ")
            newAddress = input(f"Enter new address (current: {item['address']}): ")
            item["phone"] = newPhone
            item["email"] = newEmail
            item["address"] = newAddress
            break
    if not studentFound:
        print(f"Student with name {name} not found")
    else:
        students.sort(key=lambda x: x["name"])
        print(f"Student {name} has been updated")

def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement(students_list)
                printAllList(students_list)
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement(students_list)
                printAllList(students_list)
            case "D" | "d":
                print("Element will be deleted:")
                deleteElement(students_list)
                printAllList(students_list)
            case "P" | "p":
                print("List will be printed:")
                printAllList(students_list)
            case "X" | "x":
                print("Exiting program...")
                save_data_to_csv(file_name, students_list)
                break
            case _:
                print("Wrong choice")

# Запуск основної програми
if __name__ == "__main__":
    main()
