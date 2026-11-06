
# ==========================================
# LAMBDA FUNCTIONS
# ==========================================

# 1. Simple Lambda
square = lambda x: x ** 2

print(square(5))

# 2. Addition
add = lambda a, b: a + b

print(add(10, 20))

# 3. Subtraction
sub = lambda a, b: a - b

print(sub(20, 10))

# 4. Even or Odd
check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(10))
print(check(7))

# 5. Lambda With Multiple Arguments
multiply = lambda a, b, c: a * b * c

print(multiply(2, 3, 4))

# 6. Map Function
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))

print(squares)

# 7. Filter Function
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

# 8. Sorted With Lambda
students = [
    ("Krunal", 85),
    ("Rahul", 90),
    ("Amit", 75)
]

result = sorted(students, key=lambda x: x[1])

print(result)

# 9. Sorting Dictionary Items
data = {"Apple": 50, "Banana": 20, "Mango": 80}

result = sorted(data.items(), key=lambda x: x[1])

print(result)

# 10. Reduce Function
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print(total)
