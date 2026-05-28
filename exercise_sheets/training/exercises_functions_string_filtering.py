# PYTHON EXERCISES: FOR LOOPS AND STRING FILTERING
# Instructions: Complete the functions. Use 'for' loops to iterate through strings 
# and 'if' statements to filter characters.

# --- SOLUTION EXAMPLE ---

def count_letters_x(text, letter):
    """
    Example: Count how many times a specific letter appears in the text.
    Test Case: "mommy", "m" -> 3
    """
    count = 0
    for character in text:
        if character == letter:
            count += 1
    return count


# ---------------------------------------------------------
# PART 1: ITERATION AND FOR LOOPS (10 Exercises)
# ---------------------------------------------------------

def double_characters(string):
    # 1. Return a string where each character is repeated twice.
    # Test Case: "Hello" -> "HHeelllloo"
    pass

def count_vowels(string):
    # 2. Count how many vowels (a, e, i, o, u) are present in the string.
    # Test Case: "Python" -> 1
    pass

def reverse_with_for(string):
    # 3. Reverse the string using a for loop (do not use slicing [::-1]).
    # Test Case: "Challenge" -> "egnellahC"
    pass

def only_even_positions(string):
    # 4. Create a new string using only the characters found at an even index.
    # Test Case: "Computer" -> "Cmue"
    pass

def replace_spaces(string):
    # 5. Replace every space " " with a hyphen "-" using a for loop.
    # Test Case: "A B C" -> "A-B-C"
    pass

def string_to_code_list(string):
    # 6. Transform the string into a list containing the ASCII code of each character (use ord()).
    # Test Case: "Ab" -> [65, 98]
    pass

def alternate_uppercase(string):
    # 7. Return the string with characters in even positions in uppercase and odd positions in lowercase.
    # Test Case: "house" -> "HoUsE"
    pass

def find_first_vowel(string):
    # 8. Return the index of the first vowel you encounter. If there are none, return -1.
    # Test Case: "Gym" -> -1 | "Melon" -> 1
    pass

def group_hyphens(n):
    # 9. Receive an integer n and generate a string with n groups of "*-*".
    # Test Case: 3 -> "*-**-**-*"
    pass

def count_uppercase(string):
    # 10. Count how many uppercase letters are present in the string.
    # Test Case: "ProGram" -> 2
    pass


# ---------------------------------------------------------
# PART 2: FILTERING ALGORITHMS (10 Exercises)
# ---------------------------------------------------------

def only_consonants(string):
    # 1. Return a string containing only the consonants of the original.
    # Test Case: "Informatics" -> "nfrmtcs"
    pass

def remove_punctuation(string):
    # 2. Given a string, eliminate periods, commas, and exclamation marks (.,!).
    # Test Case: "Hey! How's it going?" -> "Hey How's it going?" (ignore the question mark and apostrophe for now)
    pass

def filter_numbers(string):
    # 3. Extract only the numerical characters from a mixed string.
    # Test Case: "Code123" -> "123"
    pass

def string_without_consecutive_duplicates(string):
    # 4. Remove identical consecutive characters (e.g., "mamma" -> "mama").
    # Test Case: "Aaaabbbb" -> "Ab"
    pass

def only_long_words(text):
    # 5. (Difficult) Receive a string of words separated by spaces. 
    # Return a string containing only words longer than 3 characters.
    # Test Case: "The cat runs fast" -> "runs fast"
    pass

def filter_uppercase_string(string):
    # 6. Create a new string containing only the uppercase letters found.
    # Test Case: "uNiversitY" -> "NY"
    pass

def hide_characters(string):
    # 7. Replace every character except the first and the last one with an asterisk "*".
    # Test Case: "Secret" -> "S****t"
    pass

def extract_hexadecimals(string):
    # 8. Keep only characters that are digits (0-9) or letters from 'a' to 'f'.
    # Test Case: "gh12afz" -> "12af"
    pass

def remove_specific_vowels(string, vowels_to_remove):
    # 9. Remove from the string only the vowels indicated in the second parameter.
    # Test Case: ("Parallel", "ae") -> "Prlll"
    pass

def check_numeric_presence(string):
    # 10. Return True if the string contains at least one number, otherwise False.
    # Test Case: "User2024" -> True | "Admin" -> False
    pass
