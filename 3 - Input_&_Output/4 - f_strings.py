
# 1. Basic f-string
name = "Krunal"
age = 19

print(f"My name is {name}.")
print(f"I am {age} years old.")


# 2. Using multiple variables
city = "Ahmedabad"
course = "B.Tech CSE"

print(f"I live in {city} and study {course}.")


# 3. Performing calculations inside f-strings
a = 10
b = 20

print(f"Addition: {a + b}")
print(f"Multiplication: {a * b}")
print(f"Square of a: {a ** 2}")


# 4. Formatting decimal numbers
price = 123.4567

print(f"Price: {price:.2f}")


# 5. Formatting percentages
percentage = 0.856

print(f"Percentage: {percentage:.2%}")


# 6. Formatting numbers with leading zeros
number = 7

print(f"Number: {number:03d}")


# 7. Using expressions
length = 10
width = 5

print(f"Area of rectangle: {length * width}")


# 8. Calling methods inside f-strings
language = "python"

print(f"Uppercase: {language.upper()}")
print(f"Title case: {language.title()}")


# 9. Formatting currency
amount = 1500.5

print(f"Amount: ₹{amount:,.2f}")


# 10. Debugging with f-strings (Python 3.8+)
x = 100

print(f"{x=}")
