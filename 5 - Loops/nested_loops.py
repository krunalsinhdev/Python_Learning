
"""
nested_loops.py
Learn nested loops using tables and patterns.
"""

# 1. Print a 3 x 3 grid
print("3 x 3 Grid:")
for row in range(3):
    for column in range(3):
        print("*", end=" ")
    print()

# 2. Multiplication tables from 1 to 3
print("\nMultiplication Tables:")
for number in range(1, 4):
    print(f"\nTable of {number}")
    for multiplier in range(1, 11):
        print(f"{number} x {multiplier} = {number * multiplier}")

# 3. Right-angled triangle
print("\nStar Triangle:")
for row in range(1, 6):
    for column in range(row):
        print("*", end=" ")
    print()

# 4. Number pattern
print("\nNumber Pattern:")
for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()
