
# ==========================================
# *ARGS AND **KWARGS
# ==========================================

# 1. Basic *args
def numbers(*args):
    print(args)

numbers(10, 20, 30)

# 2. Sum Using *args
def total(*args):
    return sum(args)

print(total(10, 20, 30, 40))

# 3. Loop Through *args
def display(*args):
    for item in args:
        print(item)

display("Python", "Java", "C++")

# 4. Basic **kwargs
def student(**kwargs):
    print(kwargs)

student(name="Krunal", age=19, city="Ahmedabad")

# 5. Loop Through **kwargs
def details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

details(name="Krunal", course="Python", age=19)

# 6. Combining *args and **kwargs
def information(*args, **kwargs):
    print("Arguments:", args)
    print("Keyword Arguments:", kwargs)

information(10, 20, 30, name="Krunal", age=19)

# 7. Multiplication Using *args
def multiply(*numbers):
    result = 1

    for number in numbers:
        result *= number

    return result

print(multiply(2, 3, 4))

# 8. Finding Maximum
def maximum(*numbers):
    return max(numbers)

print(maximum(10, 50, 20, 90))

# 9. Unpacking List
values = [10, 20, 30]

def add(a, b, c):
    print(a + b + c)

add(*values)

# 10. Unpacking Dictionary
data = {"name": "Krunal", "age": 19}

def profile(name, age):
    print(name, age)

profile(**data)
