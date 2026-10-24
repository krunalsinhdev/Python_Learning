
"""
for_loop.py
Learn for loops, range(), strings, and lists.
"""

# 1. Print numbers from 1 to 5
print("Numbers from 1 to 5:")
for number in range(1, 6):
    print(number)

# 2. Print numbers from 0 to 4
print("\nNumbers from 0 to 4:")
for number in range(5):
    print(number)

# 3. Print even numbers from 2 to 10
print("\nEven numbers:")
for number in range(2, 11, 2):
    print(number)

# 4. Iterate over a string
print("\nCharacters in Python:")
for character in "Python":
    print(character)

# 5. Iterate over a list
fruits = ["Apple", "Banana", "Mango"]
print("\nFruits:")
for fruit in fruits:
    print(fruit)

# 6. Calculate the sum of numbers from 1 to 10
total = 0
for number in range(1, 11):
    total += number

print("\nSum:", total)

# 7. Multiplication table
number = 5
print(f"\nMultiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
