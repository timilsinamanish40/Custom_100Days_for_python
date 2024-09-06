import random

int_a_min = int(input("Enter the first integer: "))
int_b_max = int(input("Enter the second integer: "))

if int_a_min > int_b_max:
    print("Invalid range: minimum value is greater than maximum value.")
else:
    # Generate a random number within the valid range
    rand_num = random.randint(int_a_min, int_b_max)
    print("The Random Number is:", rand_num)

    