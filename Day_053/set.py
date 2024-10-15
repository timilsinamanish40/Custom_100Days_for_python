# Create two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union: Elements in either set_a or set_b
union_set = set_a.union(set_b)
# Or using |
union_set_alt = set_a | set_b
print("Union:", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Intersection: Elements in both set_a and set_b
intersection_set = set_a.intersection(set_b)
# Or using &
intersection_set_alt = set_a & set_b
print("Intersection:", intersection_set)  # Output: {4, 5}

# Difference: Elements in set_a but not in set_b
difference_set = set_a.difference(set_b)
# Or using -
difference_set_alt = set_a - set_b
print("Difference (A - B):", difference_set)  # Output: {1, 2, 3}

# Symmetric Difference: Elements in either set_a or set_b but not in both
symmetric_difference_set = set_a.symmetric_difference(set_b)
# Or using ^
symmetric_difference_set_alt = set_a ^ set_b
print("Symmetric Difference:", symmetric_difference_set)  # Output: {1, 2, 3, 6, 7, 8}

# Subset: Check if set_a is a subset of set_b
is_subset = set_a.issubset(set_b)
print("Is A a subset of B?", is_subset)  # Output: False

# Superset: Check if set_a is a superset of set_b
is_superset = set_a.issuperset(set_b)
print("Is A a superset of B?", is_superset)  # Output: False

# Disjoint: Check if set_a and set_b have no elements in common
is_disjoint = set_a.isdisjoint(set_b)
print("Are A and B disjoint?", is_disjoint)  # Output: False
