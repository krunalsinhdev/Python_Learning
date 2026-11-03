
# ==========================================
# PYTHON DICTIONARIES
# ==========================================

# 1. Creating Dictionary
student = {
    "name": "Krunal",
    "age": 19,
    "course": "Python",
    "marks": 90
}

print(student)

# 2. Accessing Values
print(student["name"])
print(student.get("age"))

# 3. Adding New Elements
student["city"] = "Ahmedabad"
print(student)

# 4. Updating Values
student["marks"] = 95
print(student)

# 5. Update Method
student.update({"age": 20, "course": "Core Python"})
print(student)

# 6. Removing Elements
student.pop("age")
print(student)

# 7. Popitem
student.popitem()
print(student)

# 8. Delete Element
del student["marks"]
print(student)

# 9. Dictionary Length
print(len(student))

# 10. Keys
print(student.keys())

# 11. Values
print(student.values())

# 12. Items
print(student.items())

# 13. Loop Through Dictionary
for key in student:
    print(key, student[key])

# 14. Loop Through Keys and Values
for key, value in student.items():
    print(key, ":", value)

# 15. Checking Key
print("name" in student)

# 16. Nested Dictionary
students = {
    "student1": {
        "name": "Krunal",
        "marks": 90
    },
    "student2": {
        "name": "Rahul",
        "marks": 85
    }
}

print(students["student1"]["name"])
print(students["student2"]["marks"])

# 17. Dictionary Copy
copied = student.copy()
print(copied)

# 18. Dictionary From Keys
keys = ["name", "age", "city"]
new_dict = dict.fromkeys(keys, "Unknown")
print(new_dict)

# 19. Set Default
student.setdefault("country", "India")
print(student)

# 20. Clear Dictionary
student.clear()
print(student)
