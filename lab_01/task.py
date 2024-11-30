# already sorted list
list = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "address": "123 Main St"},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "address": "456 Elm St"},
    {"name": "Jon", "phone": "0631234567", "email": "jon@example.com", "address": "789 Oak St"},
    {"name": "Zak", "phone": "0631234567", "email": "zak@example.com", "address": "101 Pine St"}
]

def printAllList():
    for elem in list:
        strForPrint = f"Student name is {elem['name']}, Phone is {elem['phone']}, Email is {elem['email']}, Address is {elem['address']}"
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    address = input("Please enter student address: ")
    newItem = {"name": name, "phone": phone, "email": email, "address": address}
    
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print(f"Delete position {deletePosition}")
        del list[deletePosition]
    return

def updateElement():
    name = input("Please enter name to be updated: ")
    
    # Find the student in the list
    studentFound = False
    for item in list:
        if item["name"] == name:
            studentFound = True
            # Update the student's details
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
        # Re-sort the list to maintain order
        list.sort(key=lambda x: x["name"])
        print(f"Student {name} has been updated")
    return

def main():
    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated:")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted:")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed:")
                printAllList()
            case "X" | "x":
                print("Exiting program...")
                break
            case _:
                print("Wrong choice")

main()
