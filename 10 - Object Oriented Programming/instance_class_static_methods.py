# Instance, Class, and Static Methods

class Employee:
    company = "Tech Solutions"

    def __init__(self, name):
        self.name = name

    def show_employee(self):  # Instance method
        print(f"Employee: {self.name}")

    @classmethod
    def show_company(cls):    # Class method
        print(f"Company: {cls.company}")

    @staticmethod
    def is_workday(day):      # Static method
        return day.lower() not in ("saturday", "sunday")

employee = Employee("Riya")
employee.show_employee()
Employee.show_company()
print("Is Monday a workday?", Employee.is_workday("Monday"))
print("Is Sunday a workday?", Employee.is_workday("Sunday"))
