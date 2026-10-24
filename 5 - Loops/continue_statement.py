
"""
continue_statement.py
Learn how to skip iterations using continue.
"""

# 1. Skip number 3
for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# 2. Print only odd numbers
print("\nOdd numbers:")
for number in range(1, 11):
    if number % 2 == 0:
        continue
    print(number)

# 3. Skip negative numbers
numbers = [10, -5, 20, -2, 30]

print("\nPositive numbers:")
for number in numbers:
    if number < 0:
        continue
    print(number)

# 4. Skip spaces in a string
text = "Hello World"

print("\nCharacters without spaces:")
for character in text:
    if character == " ":
        continue
    print(character, end="")

print()
