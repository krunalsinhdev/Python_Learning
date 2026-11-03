
# ==========================================
# PYTHON SETS
# ==========================================

# 1. Creating Sets
numbers = {10, 20, 30, 40, 50}
print(numbers)

# 2. Duplicate Values
values = {10, 20, 10, 30, 20}
print(values)  # Duplicates removed

# 3. Empty Set
empty_set = set()
print(empty_set)

# 4. Adding Elements
numbers.add(60)
print(numbers)

# 5. Adding Multiple Elements
numbers.update([70, 80, 90])
print(numbers)

# 6. Removing Elements
numbers.remove(20)
print(numbers)

numbers.discard(100)  # No error if missing
print(numbers)

numbers.pop()  # Removes an arbitrary element
print(numbers)

# 7. Set Length
print(len(numbers))

# 8. Union
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a.union(b))
print("Union Operator:", a | b)

# 9. Intersection
print("Intersection:", a.intersection(b))
print("Intersection Operator:", a & b)

# 10. Difference
print("Difference:", a.difference(b))
print("Difference Operator:", a - b)

# 11. Symmetric Difference
print(a.symmetric_difference(b))
print(a ^ b)

# 12. Subset
x = {1, 2}
y = {1, 2, 3, 4}

print(x.issubset(y))

# 13. Superset
print(y.issuperset(x))

# 14. Disjoint
print({1, 2}.isdisjoint({3, 4}))

# 15. Loop Through Set
for item in a:
    print(item)

# 16. Frozenset (Immutable Set)
fixed = frozenset([1, 2, 3, 4])
print(fixed)

# 17. Clear Set
a.clear()
print(a)
