# Constructors
# __init__() runs automatically when an object is created.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

student1 = Student("Krunal", 19)
student1.display()
