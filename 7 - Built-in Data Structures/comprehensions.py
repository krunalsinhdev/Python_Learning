
# ==========================================
# PYTHON COMPREHENSIONS
# ==========================================

# 1. Normal List Creation
squares = []

for i in range(1, 6):
    squares.append(i ** 2)

print(squares)

# 2. List Comprehension
squares = [i ** 2 for i in range(1, 6)]
print(squares)

# 3. Even Numbers
even = [i for i in range(1, 21) if i % 2 == 0]
print(even)

# 4. Odd Numbers
odd = [i for i in range(1, 21) if i % 2 != 0]
print(odd)

# 5. If-Else Comprehension
result = [
    "Even" if i % 2 == 0 else "Odd"
    for i in range(1, 11)
]

print(result)

# 6. String Comprehension
words = ["python", "java", "c++"]

upper_words = [word.upper() for word in words]
print(upper_words)

# 7. Set Comprehension
numbers = [1, 2, 2, 3, 3, 4]

unique = {i for i in numbers}
print(unique)

# 8. Dictionary Comprehension
squares = {i: i ** 2 for i in range(1, 6)}
print(squares)

# 9. Dictionary With Condition
even_squares = {
    i: i ** 2
    for i in range(1, 11)
    if i % 2 == 0
}

print(even_squares)

# 10. Nested List Comprehension
matrix = [[i * j for j in range(1, 4)]
          for i in range(1, 4)]

print(matrix)

# 11. Flatten Nested List
nested = [[1, 2], [3, 4], [5, 6]]

flat = [item for sublist in nested for item in sublist]
print(flat)

# 12. Generator Expression
numbers = (i ** 2 for i in range(1, 6))

for number in numbers:
    print(number)
