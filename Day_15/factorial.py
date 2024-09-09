# n! = n * (n - 1) * (n - 2) * ... * 1
# So, initialize the result as 1 and multiply it by each integer from 1 to n

def factorial(n):
    result = 1  

    # Iterate from 1 to n
    for i in range(1, n + 1):
        result *= i 
    return result 
