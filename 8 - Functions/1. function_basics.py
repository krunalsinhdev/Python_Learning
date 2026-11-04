
# ==========================================
# PYTHON FUNCTION BASICS
# ==========================================

# 1. Creating a Simple Function
def greet():
    print("Hello, Welcome to Python!")

# Calling Function
greet()

# 2. Function With Multiple Calls
def welcome():
    print("Welcome Krunal")

welcome()
welcome()
welcome()

# 3. Function With Parameters
def greet_user(name):
    print("Hello", name)

greet_user("Krunal")
greet_user("Rahul")

# 4. Function With Multiple Parameters
def student(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student("Krunal", 19, "Python")

# 5. Function With Return Value
def addition(a, b):
    return a + b

result = addition(10, 20)
print("Addition:", result)

# 6. Function Without Return
def display():
    print("Learning Functions")

result = display()
print("Return value:", result)  # None

# 7. Built-in Functions
print(len("Python"))
print(max(10, 20, 30))
print(min(10, 20, 30))
print(sum([10, 20, 30]))

# 8. Function With Condition
def check_number(number):
    if number > 0:
        print("Positive Number")
    elif number < 0:
        print("Negative Number")
    else:
        print("Zero")

check_number(10)
check_number(-5)
check_number(0)

# 9. Function Returning Multiple Values
def calculate(a, b):
    return a + b, a - b, a * b

add, sub, mul = calculate(10, 5)

print(add)
print(sub)
print(mul)

# 10. Function as a Reusable Calculator
def calculator(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

calculator(20, 10)
