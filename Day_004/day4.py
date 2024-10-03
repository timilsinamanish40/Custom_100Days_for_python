# Task 1: Perform basic arithmetic operations on two integers
num1 = 10
num2 = 5

# Perform basic arithmetic operations
addition = num1 + num2
# subtraction = num1 - num2
# multiplication = num1 * num2
# division = num1 / num2

# Print the results to the console
print("Arithmetic Operations:")
# print("Addition:", addition)
# print("Subtraction:", subtraction)
# print("Multiplication:", multiplication)
# print("Division:", division)
print()  # Blank line for separation

# Task 2: Calculate the area of a rectangle with integer inputs
length_int = int(input("Enter the length of the rectangle (integer): "))
width_int = int(input("Enter the width of the rectangle (integer): "))

# Calculate the area of the rectangle
area_int = length_int * width_int

# Print the result
print("The area of the rectangle (integer inputs) is:", area_int)
print()  # Blank line for separation

# Task 3: Calculate the area of a rectangle with decimal inputs and formatted output
length_float = float(input("Enter the length of the rectangle (decimal): "))
width_float = float(input("Enter the width of the rectangle (decimal): "))

# Calculate the area of the rectangle
area_float = length_float * width_float

# Print the result with two decimal points
print(f"The area of the rectangle (decimal inputs) is: {area_float:.2f}")
