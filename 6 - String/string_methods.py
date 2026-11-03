
# Python String Methods

text = "  hello python programming  "

# Case conversion
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.swapcase())

# Removing spaces
print(text.strip())
print(text.lstrip())
print(text.rstrip())

# Searching
print(text.find("python"))
print(text.index("python"))
print(text.count("o"))

# Replacing
print(text.replace("python", "java"))

# Splitting and joining
languages = "Python,Java,C,C++"
print(languages.split(","))

words = ["I", "Love", "Python"]
print(" ".join(words))

# Checking string content
print("Python".isalpha())
print("12345".isdigit())
print("Python123".isalnum())
print("hello".islower())
print("HELLO".isupper())
print("Hello World".istitle())
print("   ".isspace())

# Checking start and end
print("Python Programming".startswith("Python"))
print("Python Programming".endswith("Programming"))
