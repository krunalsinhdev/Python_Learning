
# ==========================================
# IMPORTING MODULES ..
# ==========================================

# 1. Import Complete Module
import math

print(math.sqrt(64))

# 2. Import With Alias
import math as m

print(m.factorial(5))
print(m.pi)

# 3. Import Specific Function
from math import sqrt

print(sqrt(100))

# 4. Import Multiple Functions
from math import sqrt, factorial, pi

print(sqrt(81))
print(factorial(4))
print(pi)

# 5. Import With Alias
from math import factorial as fact

print(fact(5))

# 6. Import All (Not Recommended)
# from math import *
# Avoid this because it can create naming conflicts.

# 7. Import Random Module
import random

print(random.randint(1, 10))

# 8. Module Name
import datetime

print(datetime.__name__)

# 9. Module Location
print(datetime.__file__)

# 10. Available Module Attributes
print(dir(math))
