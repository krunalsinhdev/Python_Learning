
# 1. Using the format() method
name = "Krunal"
age = 19

print("My name is {} and I am {} years old.".format(name, age))


# 2. Using positional indexes
print("My name is {0} and my age is {1}.".format(name, age))
print("My age is {1} and my name is {0}.".format(name, age))


# 3. Using named placeholders
print("Name: {n}, Age: {a}".format(n=name, a=age))


# 4. Formatting decimal numbers
price = 123.4567
print("Price: {:.2f}".format(price))


# 5. Formatting numbers with leading zeros
number = 7
print("Number: {:03d}".format(number))


# 6. Formatting percentages
percentage = 0.856
print("Percentage: {:.2%}".format(percentage))


# 7. Using old-style % formatting
student = "Krunal"
marks = 85

print("Student: %s" % student)
print("Marks: %d" % marks)
print("Student %s scored %d marks." % (student, marks))


# 8. Formatting floating-point numbers with %
average = 87.456
print("Average: %.2f" % average)


# 9. Aligning text
print("{:<10}".format("Python"))  # Left aligned
print("{:>10}".format("Python"))  # Right aligned
print("{:^10}".format("Python"))  # Center aligned
