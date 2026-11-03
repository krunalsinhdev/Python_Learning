
# ==========================================
# PYTHON LISTS
# ==========================================

# 1. Creating a List
numbers = [10, 20, 30, 40, 50]
names = ["Krunal", "Rahul", "Amit"]
mixed = [10, "Python", 20.5, True]

print("Numbers:", numbers)
print("Names:", names)
print("Mixed:", mixed)

# 2. Accessing Elements
print(numbers[0])
print(numbers[-1])

# 3. Updating Elements
numbers[1] = 200
print("Updated:", numbers)

# 4. Adding Elements
numbers.append(60)
print("Append:", numbers)

numbers.insert(1, 15)
print("Insert:", numbers)

numbers.extend([70, 80, 90])
print("Extend:", numbers)

# 5. Removing Elements
numbers.remove(200)
print("Remove:", numbers)

numbers.pop()
print("Pop:", numbers)

del numbers[0]
print("Delete:", numbers)

# 6. List Length
print("Length:", len(numbers))

# 7. Searching
print("Index:", numbers.index(30))
print("Count:", numbers.count(30))
print("Exists:", 30 in numbers)

# 8. Sorting
values = [50, 10, 40, 20, 30]

values.sort()
print("Ascending:", values)

values.sort(reverse=True)
print("Descending:", values)

# 9. Reversing
values.reverse()
print("Reversed:", values)

# 10. Copying a List
original = [1, 2, 3, 4]
copied = original.copy()

print("Original:", original)
print("Copied:", copied)

# 11. Clearing a List
copied.clear()
print("Cleared:", copied)

# 12. Loop Through List
fruits = ["Apple", "Mango", "Banana"]

for fruit in fruits:
    print(fruit)

# 13. Nested List
students = [
    ["Krunal", 85],
    ["Rahul", 90],
    ["Amit", 78]
]

print("Student:", students[0][0])
print("Marks:", students[0][1])

# 14. List Slicing
data = [10, 20, 30, 40, 50, 60]

print(data[0:3])
print(data[2:])
print(data[:4])
print(data[::-1])

# 15. List Unpacking
a, b, c = [10, 20, 30]

print(a, b, c)
