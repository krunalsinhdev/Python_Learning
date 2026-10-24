
"""
pass_statement.py
Learn the pass statement.
"""

# 1. Empty for loop
for number in range(5):
    pass

print("The loop completed.")

# 2. Empty while loop body
count = 0
while count < 3:
    pass  # Placeholder only; avoid this in real code.
    count += 1

print("While loop completed.")

# 3. Placeholder for a future function
def calculate_total():
    pass

print("Function is defined but not implemented.")

# 4. Placeholder in a conditional statement
age = 20

if age >= 18:
    pass  # Add adult-related logic later.
else:
    print("You are under 18.")

# 5. Placeholder in a class
class Student:
    pass

student = Student()
print("Student object created:", isinstance(student, Student))
