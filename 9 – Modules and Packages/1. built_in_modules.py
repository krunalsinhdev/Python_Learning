
# ==========================================
# PYTHON BUILT-IN MODULES
# ==========================================

# 1. Math Module
import math

print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Factorial:", math.factorial(5))
print("Ceil:", math.ceil(4.3))
print("Floor:", math.floor(4.8))
print("Pi:", math.pi)

# 2. Random Module
import random

print("Random Number:", random.randint(1, 100))
print("Random Choice:", random.choice(["Python", "Java", "C++"]))

numbers = [10, 20, 30, 40]
random.shuffle(numbers)
print("Shuffled:", numbers)

print("Random Float:", random.random())

# 3. Datetime Module
import datetime

current = datetime.datetime.now()
print("Current Date and Time:", current)
print("Year:", current.year)
print("Month:", current.month)
print("Day:", current.day)

# 4. Calendar Module
import calendar

print(calendar.month(2026, 11))
print("Leap Year:", calendar.isleap(2024))

# 5. Statistics Module
import statistics

data = [10, 20, 30, 40, 50]

print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
print("Mode:", statistics.mode([10, 20, 20, 30]))

# 6. OS Module
import os

print("Current Directory:", os.getcwd())
print("Directory Contents:", os.listdir("."))

# 7. Sys Module
import sys

print("Python Version:", sys.version)
print("Platform:", sys.platform)

# 8. String Module
import string

print("Letters:", string.ascii_letters)
print("Digits:", string.digits)
print("Punctuation:", string.punctuation)

# 9. Collections Module
from collections import Counter

items = ["Python", "Java", "Python", "C++", "Python"]
print("Frequency:", Counter(items))

# 10. Time Module
import time

print("Current Timestamp:", time.time())
print("Readable Time:", time.ctime())
