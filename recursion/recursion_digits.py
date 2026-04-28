def count_digits(n):    
    # Base Case: n // 10 being 0 means n is a single-digit number
    if n // 10 == 0:
        return 1
    
    # Recursive Step: Count this digit (1) + the rest of the digits
    return 1 + count_digits(n // 10)

print(count_digits(1000000))

# call1: 1 + 2 = 3
# call2: 1 + 1 = 2
# call3: 1