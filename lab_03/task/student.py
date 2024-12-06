class Student:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Student(name={self.name}, phone={self.phone}, email={self.email}, address={self.address})"
