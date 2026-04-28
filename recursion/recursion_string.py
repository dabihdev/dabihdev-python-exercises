def recursive_length(s):
    # Base case: an empty string has length 0
    if s == "":
        return 0
    
    # Recursive step: 1 + length of the string excluding the first character
    return 1 + recursive_length(s[1:])

# Example usage:
# my_string = "Hello"
# print(f"The length of '{my_string}' is: {recursive_length(my_string)}")

def count_char(s, c):
    # 1. Base Case: If the string is empty, we stop
    if s == "":
        return 0
    
    # 2. Recursive Step: Check the first character
    if s[0] == c:
        # It's a match! Add 1 and check the rest of the string
        return 1 + count_char(s[1:], c)
    else:
        # No match. Add 0 and check the rest of the string
        return 0 + count_char(s[1:], c)

# Testing the function
result = count_char("baab", "a")
print(f"The character appears {result} times.")