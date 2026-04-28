def is_perfect(n):
    # check all numbers from 1 to n, if they are proper divisors
    divisor = 1
    sum = 0
    
    while divisor < n:
        if n % divisor == 0:
            print("proper divisor is ", divisor)
            sum += divisor # add the proper divisor to the total
        divisor += 1 # go on with the numbers
    
    # we need to check if the sum of the divisors is equal n
    if sum == n:
        return True
    else:
        return False

print(is_perfect(496))