
# String Practice Questions

# 1. Reverse a string
text = "Python"
print("Reverse:", text[::-1])

# 2. Check palindrome
word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 3. Count vowels
text = "Hello Python"
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Vowels:", count)

# 4. Count characters
text = "Python Programming"
print("Total characters:", len(text))

# 5. Count words
text = "I love learning Python"
words = text.split()
print("Total words:", len(words))

# 6. Convert first letter to uppercase
text = "python programming"
print(text.title())

# 7. Remove spaces
text = "Python Programming"
print(text.replace(" ", ""))

# 8. Count a particular character
text = "programming"
print("Count of m:", text.count("m"))

# 9. Check whether string contains Python
text = "I am learning Python"

if "Python" in text:
    print("Found")
else:
    print("Not Found")

# 10. Remove duplicate characters
text = "programming"
result = ""

for char in text:
    if char not in result:
        result += char

print("Without duplicates:", result)
