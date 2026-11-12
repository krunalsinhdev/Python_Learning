# Instance Variables and Class Variables

class Student:
    college = "ABC College"  # Class variable: shared by all objects

    def __init__(self, name, roll_no):
        self.name = name       # Instance variable: unique to each object
        self.roll_no = roll_no

    def display(self):
        print(f"{self.name} | Roll No: {self.roll_no} | College: {self.college}")

student1 = Student("Aarav", 101)
student2 = Student("Diya", 102)

student1.display()
student2.display()

Student.college = "XYZ University"
print("\nAfter changing the class variable:")
student1.display()
student2.display()
