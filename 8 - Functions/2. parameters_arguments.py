
# ==========================================
# PARAMETERS AND ARGUMENTS
# ==========================================

# 1. Positional Arguments
def student(name, age):
    print("Name:", name)
    print("Age:", age)

student("Krunal", 19)

# 2. Multiple Positional Arguments
def addition(a, b, c):
    print("Addition:", a + b + c)

addition(10, 20, 30)

# 3. Keyword Arguments
def employee(name, salary):
    print("Name:", name)
    print("Salary:", salary)

employee(name="Krunal", salary=25000)

# 4. Positional and Keyword Arguments
def details(name, city):
    print(name, city)

details("Krunal", city="Ahmedabad")

# 5. Variable-Length Positional Arguments
def total(*numbers):
    print("Numbers:", numbers)
    print("Total:", sum(numbers))

total(10, 20)
total(10, 20, 30, 40)

# 6. Variable-Length Keyword Arguments
def information(**details):
    for key, value in details.items():
        print(key, ":", value)

information(name="Krunal", age=19, city="Ahmedabad")

# 7. Unpacking a List
def add(a, b, c):
    print(a + b + c)

values = [10, 20, 30]
add(*values)

# 8. Unpacking a Dictionary
def display(name, age):
    print(name, age)

data = {"name": "Krunal", "age": 19}
display(**data)

# 9. Argument Order
def profile(name, course, city):
    print(name, course, city)

profile("Krunal", "Python", "Ahmedabad")

# 10. Type Hints in Parameters
def multiply(a: int, b: int) -> int:
    return a * b

print(multiply(5, 4))
