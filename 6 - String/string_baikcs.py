
# String Basics in Python

# Creating strings
name = "Krunal"
city = 'Ahmedabad'
message = """Welcome to Python Learning"""

print(name)
print(city)
print(message)

# String length
print("Length:", len(name))

# Accessing characters
print("First character:", name[0])
print("Last character:", name[-1])

# String concatenation
first_name = "Krunal"
last_name = "Dodiya"

full_name = first_name + " " + last_name
print("Full Name:", full_name)

# String repetition
print("Python " * 3)

# Checking substring
text = "I am learning Python"

print("Python" in text)
print("Java" not in text)

# Strings are immutable
# name[0] = "M"  # This will give an error
