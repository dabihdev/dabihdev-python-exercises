def factorial(n):
    # 1. Base Case: if n is 1 or 0, we stop
    if n <= 1:
        return 1

    # 2. Recursive Step: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

print(f"Result of the recursive factorial: {factorial(5)}") # Output: 120

# call1: 5 * 24 = 120 --> final result
# call2: 4 * 6 = 24
# call3: 3 * 2 = 6
# call4: 2 * 1 = 2
# call5: 1



# 5! --> 5*4*3*2*1
def factorial_loop(n):
    i = n
    result = 1
    while i > 0:
        result *= i
        i -= 1 # decrease the number
    return result

print(f"Result of the factorial loop: {factorial_loop(5)}")