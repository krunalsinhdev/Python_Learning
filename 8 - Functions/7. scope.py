
# ==========================================
# VARIABLE SCOPE
# ==========================================

# 1. Global Variable
name = "Krunal"

def display():
    print(name)

display()

# 2. Local Variable
def student():
    age = 19
    print(age)

student()

# 3. Global and Local Variables
x = 100

def example():
    x = 50
    print("Local:", x)

example()
print("Global:", x)

# 4. Global Keyword
count = 0

def increase():
    global count
    count += 1

increase()
increase()

print("Count:", count)

# 5. Local Scope
def calculate():
    number = 10
    result = number * 2
    print(result)

calculate()

# 6. Nested Function
def outer():
    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()

outer()

# 7. Enclosing Scope
def outer():
    message = "Hello"

    def inner():
        print(message)

    inner()

outer()

# 8. Nonlocal Keyword
def counter():
    count = 0

    def increase():
        nonlocal count
        count += 1
        print(count)

    increase()
    increase()

counter()

# 9. LEGB Scope Demonstration
x = "Global"

def outer():
    x = "Enclosing"

    def inner():
        x = "Local"
        print(x)

    inner()

outer()

# 10. Built-in Scope
def example():
    print(len("Python"))
    print(max(10, 20, 30))

example()
