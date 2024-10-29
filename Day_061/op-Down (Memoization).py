def fibonacci_memo(n, memo={}):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Check if result is already in memo
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    
    return memo[n]

# Example usage
n = 10
print(f"Fibonacci of {n} (Memoization):", fibonacci_memo(n))
