name = input("Enter a string: ")
print("Original string:", name)
r_name = ""
# Reversing the string
for char in name:
    r_name = char + r_name 

print("Reversed string:", r_name)

# Initialization:
# r_name is initialized as an empty string: r_name = "".
# First Iteration:

# char = 'a' (the first character of the string name).
# r_name = char + r_name → r_name = 'a' + "" → r_name = "a".

# Second Iteration:
# char = 'b' (the second character of name).
# r_name = char + r_name → r_name = 'b' + "a" → r_name = "ba".

# Third Iteration:
# char = 'c' (the third character of name).
# r_name = char + r_name → r_name = 'c' + "ba" → r_name = "cba".
