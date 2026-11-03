
# String Indexing and Slicing

text = "PYTHON PROGRAMMING"

# Positive indexing
print(text[0])
print(text[1])
print(text[2])

# Negative indexing
print(text[-1])
print(text[-2])
print(text[-3])

# Slicing
print(text[0:6])
print(text[7:18])
print(text[:6])
print(text[7:])
print(text[:])

# Step slicing
print(text[::1])
print(text[::2])
print(text[::-1])

# Reverse string
reverse_text = text[::-1]
print("Reversed:", reverse_text)
