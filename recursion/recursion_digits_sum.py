def sum_digits(n):
    # Base case: if the number is a single digit, just return it
    if n < 10:
        return n
    else:
        # Recursive step: 
        # n % 10 grabs the last digit
        last_digit = (n % 10)
        # n // 10 removes the last digit and moves the recursion forward
        return last_digit + sum_digits(n // 10)

# Example usage:
number = 1234
result = sum_digits(number)
print(f"The sum of digits in {number} is: {result}")