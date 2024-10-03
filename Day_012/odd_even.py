#program to check if a number is even or odd.
#Logic = num %2 == 0 (is even) or num %2 != 0 (is odd)

num = int(input("Enter a number to be tested : "))

if num == 0:
     print(" The number can't be Zero ")
elif num % 2 == 0:
    print(" The number is even ")
else:
    print(" The number is odd ")