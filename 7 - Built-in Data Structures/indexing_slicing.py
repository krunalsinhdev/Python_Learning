
# ==========================================
# INDEXING AND SLICING
# ==========================================

# 1. List Indexing
numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[1])
print(numbers[-1])
print(numbers[-2])

# 2. List Slicing
print(numbers[0:3])
print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[:])

# 3. Step Slicing
print(numbers[::1])
print(numbers[::2])
print(numbers[::-1])

# 4. Tuple Indexing
data = (100, 200, 300, 400, 500)

print(data[0])
print(data[-1])
print(data[1:4])

# 5. String Indexing
name = "PYTHON"

print(name[0])
print(name[-1])

# 6. String Slicing
print(name[0:3])
print(name[2:])
print(name[::-1])

# 7. Nested List Indexing
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])
print(matrix[1][1])
print(matrix[2][2])

# 8. Negative Step
values = [1, 2, 3, 4, 5, 6]

print(values[5:1:-1])
print(values[::-2])

# 9. Copy Using Slicing
original = [10, 20, 30]
copied = original[:]

print(copied)

# 10. Common Index Error
# print(numbers[10])
# IndexError: list index out of range
