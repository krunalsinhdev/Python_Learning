
# ==========================================
# RECURSION IN PYTHON
# ==========================================

# 1. Simple Recursion
def countdown(n):
    if n == 0:
        print("Done!")
        return

    print(n)
    countdown(n - 1)

countdown(5)

# 2. Factorial Using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)

print("Factorial:", factorial(5))

# 3. Sum of Natural Numbers
def natural_sum(n):
    if n == 0:
        return 0

    return n + natural_sum(n - 1)

print(natural_sum(5))

# 4. Fibonacci Series
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i), end=" ")

print()

# 5. Power Using Recursion
def power(base, exponent):
    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)

print(power(2, 5))

# 6. Reverse a String
def reverse(text):
    if len(text) <= 1:
        return text

    return reverse(text[1:]) + text[0]

print(reverse("Python"))

# 7. Sum of Digits
def digit_sum(n):
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)

print(digit_sum(12345))

# 8. Greatest Common Divisor
def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

print(gcd(48, 18))

# 9. Palindrome Check
def palindrome(text):
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return palindrome(text[1:-1])

print(palindrome("madam"))

# 10. Recursive List Sum
def list_sum(numbers):
    if not numbers:
        return 0

    return numbers[0] + list_sum(numbers[1:])

print(list_sum([10, 20, 30, 40]))
