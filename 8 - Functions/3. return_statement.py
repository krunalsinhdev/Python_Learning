
# ==========================================
# RETURN STATEMENT
# ==========================================

# 1. Simple Return
def addition(a, b):
    return a + b

print(addition(10, 20))

# 2. Return Subtraction
def subtraction(a, b):
    return a - b

print(subtraction(20, 10))

# 3. Return Multiplication
def multiplication(a, b):
    return a * b

print(multiplication(5, 4))

# 4. Return Division
def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

print(division(20, 5))
print(division(10, 0))

# 5. Returning String
def greeting(name):
    return f"Hello {name}, Welcome!"

message = greeting("Krunal")
print(message)

# 6. Returning Multiple Values
def calculate(a, b):
    return a + b, a - b, a * b

add, sub, mul = calculate(10, 5)

print(add, sub, mul)

# 7. Return With Condition
def check_even(number):
    if number % 2 == 0:
        return True
    return False

print(check_even(10))
print(check_even(7))

# 8. Early Return
def check_age(age):
    if age < 18:
        return "Not Eligible"

    return "Eligible"

print(check_age(19))

# 9. Returning a List
def get_numbers():
    return [10, 20, 30, 40, 50]

numbers = get_numbers()
print(numbers)

# 10. Returning a Dictionary
def student():
    return {
        "name": "Krunal",
        "age": 19,
        "course": "Python"
    }

data = student()
print(data)
print(data["name"])
