
# ==========================================
# KEYWORD ARGUMENTS
# ==========================================

# 1. Basic Keyword Arguments
def student(name, age):
    print(name, age)

student(name="Krunal", age=19)

# 2. Change Argument Order
student(age=20, name="Rahul")

# 3. Positional Arguments
def addition(a, b):
    print(a + b)

addition(10, 20)

# 4. Keyword Arguments
addition(a=10, b=20)

# 5. Mixed Arguments
def employee(name, salary, city):
    print(name, salary, city)

employee("Krunal", salary=25000, city="Ahmedabad")

# 6. Multiple Keyword Arguments
def details(name, age, course, city):
    print(name, age, course, city)

details(
    name="Krunal",
    age=19,
    course="Python",
    city="Ahmedabad"
)

# 7. Keyword Arguments With Defaults
def greet(name, message="Welcome"):
    print(message, name)

greet(name="Krunal")
greet(name="Rahul", message="Hello")

# 8. Dictionary Unpacking
def profile(name, age, city):
    print(name, age, city)

data = {
    "name": "Krunal",
    "age": 19,
    "city": "Ahmedabad"
}

profile(**data)

# 9. Keyword-Only Arguments
def calculate(a, b, *, operation):
    if operation == "add":
        return a + b
    elif operation == "multiply":
        return a * b

print(calculate(10, 20, operation="add"))
print(calculate(10, 20, operation="multiply"))

# 10. Common Mistake
# student(name="Krunal", 19)
# SyntaxError: Positional argument follows keyword argument
