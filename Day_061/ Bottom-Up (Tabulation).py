def fibonacci_tab(n):
    # Handle base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize base values in the table
    fib_table = [0] * (n + 1)
    fib_table[1] = 1
    
    # Fill in the table iteratively
    for i in range(2, n + 1):
        fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
    
    return fib_table[n]

# Example usage
n = 10
print(f"Fibonacci of {n} (Tabulation):", fibonacci_tab(n))
