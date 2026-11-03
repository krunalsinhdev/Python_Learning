
# ==========================================
# PYTHON TUPLES
# ==========================================

# 1. Creating Tuples
numbers = (10, 20, 30, 40, 50)
names = ("Krunal", "Rahul", "Amit")

print(numbers)
print(names)

# 2. Single Element Tuple
single = (10,)
print(single)

# 3. Without Parentheses
data = 10, 20, 30
print(data)

# 4. Accessing Elements
print(numbers[0])
print(numbers[-1])

# 5. Tuple Slicing
print(numbers[1:4])
print(numbers[::-1])

# 6. Tuple Length
print(len(numbers))

# 7. Tuple Methods
values = (10, 20, 10, 30, 10)

print("Count:", values.count(10))
print("Index:", values.index(20))

# 8. Checking Elements
print(20 in values)
print(100 not in values)

# 9. Tuple Concatenation
a = (1, 2, 3)
b = (4, 5, 6)

print(a + b)

# 10. Tuple Repetition
print(a * 3)

# 11. Tuple Unpacking
student = ("Krunal", 19, "Python")

name, age, course = student

print(name)
print(age)
print(course)

# 12. Nested Tuples
data = ((1, 2), (3, 4), (5, 6))
print(data[0][1])

# 13. Converting List into Tuple
my_list = [10, 20, 30]
my_tuple = tuple(my_list)

print(my_tuple)

# 14. Converting Tuple into List
new_list = list(my_tuple)
print(new_list)

# 15. Immutability
# numbers[0] = 100
# This gives TypeError because tuples cannot be modified.
