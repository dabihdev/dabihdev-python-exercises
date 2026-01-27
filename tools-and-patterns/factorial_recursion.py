def factorial(n):
    # 1. Base Case: if n is 1 or 0, we stop
    if n <= 1:
        return 1

    # 2. Recursive Step: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

print(factorial(5)) # Output: 120
