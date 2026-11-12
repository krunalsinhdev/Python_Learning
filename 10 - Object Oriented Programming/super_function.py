# super()
# super() calls a method from the parent class.

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)  # Call parent constructor
        self.course = course

    def introduce(self):
        super().introduce()     # Call parent method
        print(f"I study {self.course}.")

student = Student("Krunal", "Computer Science")
student.introduce()
