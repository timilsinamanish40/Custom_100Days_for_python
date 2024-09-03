# Reading the percentage as input
percentage = float(input("Enter your percentage: "))

# Determining the letter grade
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

# Printing the corresponding letter grade
print(f"Your letter grade is: {grade}")
