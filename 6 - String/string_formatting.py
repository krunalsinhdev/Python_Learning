
# String Formatting

name = "Krunal"
age = 19
language = "Python"

# Using f-string
print(f"My name is {name}")
print(f"My age is {age}")
print(f"I am learning {language}")

# Using format()
print("My name is {} and my age is {}".format(name, age))

# Using index
print("Name: {0}, Age: {1}".format(name, age))

# Formatting numbers
price = 99.5678
print(f"Price: {price:.2f}")

# Expressions in f-string
a = 10
b = 20
print(f"Addition: {a + b}")

# Alignment
print(f"{name:<15}")
print(f"{name:>15}")
print(f"{name:^15}")
