
"""
break_statement.py
Learn how to stop a loop using break.
"""

# 1. Stop when the number reaches 5
for number in range(1, 11):
    if number == 5:
        break
    print(number)

# 2. Find a number in a list
numbers = [10, 20, 30, 40, 50]
target = 30

for number in numbers:
    if number == target:
        print(f"\nFound {target}!")
        break
    print("Checking:", number)

# 3. Stop a while loop
count = 1

while count <= 10:
    if count == 6:
        print("Loop stopped at 6.")
        break

    print(count)
    count += 1

# 4. Search for a character
text = "Python Programming"
target = "P"

for character in text:
    if character == target:
        print(f"\nCharacter '{target}' found!")
        break
