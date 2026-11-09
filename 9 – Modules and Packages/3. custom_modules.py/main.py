
# ==========================================
# IMPORTING CUSTOM MODULES
# ==========================================

# 1. Import Complete Module
import calculator

print(calculator.addition(10, 20))
print(calculator.subtraction(20, 10))

# 2. Import Specific Function
from calculator import multiplication

print(multiplication(5, 4))

# 3. Import With Alias
import calculator as calc

print(calc.division(20, 5))

# 4. Import Multiple Functions
from calculator import addition, subtraction

print(addition(100, 50))
print(subtraction(100, 50))

# 5. Import Variable
print("PI:", calculator.PI)

# 6. Import Greetings Module
import greetings

print(greetings.greet("Krunal"))
print(greetings.goodbye("Krunal"))
greetings.welcome()
