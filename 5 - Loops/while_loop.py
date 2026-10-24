
"""
while_loop.py
Learn while loops and loop conditions.
"""

# 1. Print numbers from 1 to 5
number = 1
while number <= 5:
    print(number)
    number += 1

# 2. Countdown
print("\nCountdown:")
count = 5
while count >= 1:
    print(count)
    count -= 1
print("Go!")

# 3. Sum of numbers from 1 to 10
number = 1
total = 0

while number <= 10:
    total += number
    number += 1

print("\nSum:", total)

# 4. Print even numbers from 2 to 10
number = 2
print("\nEven numbers:")
while number <= 10:
    print(number)
    number += 2

# 5. User input example
# Enter 0 to stop entering numbers.
total = 0

while True:
    value = int(input("\nEnter a number (0 to stop): "))

    if value == 0:
        break

    total += value

print("Total of entered numbers:", total)
