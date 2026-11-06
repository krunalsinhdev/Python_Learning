
# ==========================================
# PYTHON DOCSTRINGS
# ==========================================

# 1. Basic Docstring
def greet():
    """Display a welcome message."""
    print("Welcome to Python")

greet()

# 2. Accessing Docstring
print(greet.__doc__)

# 3. Function With Parameters
def addition(a, b):
    """
    Add two numbers.

    Parameters:
        a: First number
        b: Second number

    Returns:
        Sum of two numbers.
    """
    return a + b

print(addition(10, 20))

# 4. Multi-line Docstring
def student(name, age):
    """
    Display student information.

    Args:
        name: Student name
        age: Student age
    """
    print(name, age)

student("Krunal", 19)

# 5. Help Function
help(addition)

# 6. Function Documentation
def square(number):
    """Return the square of a number."""
    return number ** 2

print(square.__doc__)

# 7. Type Annotations
def multiply(a: int, b: int) -> int:
    """Multiply two integers."""
    return a * b

print(multiply(5, 4))

# 8. Annotations
print(multiply.__annotations__)

# 9. Function Name
print(multiply.__name__)

# 10. Complete Documented Function
def calculate_area(length: float, width: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
        length: Length of rectangle.
        width: Width of rectangle.

    Returns:
        Rectangle area.
    """
    return length * width

area = calculate_area(10, 5)

print("Area:", area)
print("Documentation:", calculate_area.__doc__)
