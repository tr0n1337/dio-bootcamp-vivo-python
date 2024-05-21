# UNION
set_a = {1, 2}
set_b = {3, 4}

union = set_a.union(set_b)
print(f"Union: {union}")

# INTERSECTION
set_a = {1, 2, 3}
set_b = {2, 3, 4}

intersection = set_a.intersection(set_b)
print(f"Intersection: {intersection}")

# DIFFERENCE
set_a = {1, 2, 3}
set_b = {2, 3, 4}

difference_1 = set_a.difference(set_b)
difference_2 = set_b.difference(set_a)
print(f"Difference 1: {difference_1}")
print(f"Difference 2: {difference_2}")

# SYMMETRIC DIFFERENCE
set_a = {1, 2, 3}
set_b = {2, 3, 4}

symmetric_difference_1 = set_a.symmetric_difference(set_b)
print(f"Symmetric difference: {symmetric_difference_1}")

# ISSUBSET
set_a = {1, 2, 3}
set_b = {2, 3, 4}

issubset_a = set_a.issubset(set_b)
issubset_b = set_b.issubset(set_a)
print(f"ISSUBSET A: {issubset_a}")
print(f"ISSUBSET B: {issubset_b}")

# ISSUPERSET
set_a = {1, 2, 3}
set_b = {4, 1, 2, 5, 6, 3}

issuperset_a = set_a.issuperset(set_b)
issuperset_b = set_b.issuperset(set_a)
print(f"ISSUPERSET A: {issuperset_a}")
print(f"ISSUPERSET B: {issuperset_b}")

# ISDISJOINT
set_a = {1, 2, 3, 4, 5}
set_b = {6, 7, 8, 9}
set_c = {1, 0}

isdisjoint_a = set_a.isdisjoint(set_b)
isdisjoint_b = set_a.isdisjoint(set_c)
print(f"ISDISJOINT A: {isdisjoint_a}")
print(f"ISDISJOINT B: {isdisjoint_b}")

# ADD
prize = {1, 23}

prize.add(25)
print(f"ADD 1: {prize}")
prize.add(42)
print(f"ADD 2: {prize}")
prize.add(25)
print(f"ADD 3: {prize}")

# CLEAR
prize = {1, 23}
prize.clear()

print(f"CLEAR: {prize}")

# COPY
prize = {1, 23}
prize_copy = prize.copy()
print(f"COPY: {prize_copy}")

# DISCARD
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(f"DISCARD: {numbers}")
numbers.discard(1)
print(f"DISCARD: {numbers}")
numbers.discard(45)
print(f"DISCARD: {numbers}")

# POP
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(f"POP: {numbers}")
numbers.pop()
print(f"POP: {numbers}")
numbers.pop()
print(f"POP: {numbers}")

# REMOVE
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(f"REMOVE: {numbers}")
numbers.remove(0)
print(f"REMOVE: {numbers}")

# LEN
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(f"LEN: {len(numbers)}")

# IN
numbers = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}
print(f"IN: {1 in numbers}")
print(f"IN: {10 in numbers}")
