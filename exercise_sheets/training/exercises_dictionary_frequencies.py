# exercises_dictionary_frequencies.py

"""
PYTHON EXERCISES: THE COUNTING PATTERN
Focus: Using dictionaries to map frequencies and occurrences.
"""

# EXERCISE 1: Basic Character Counting
# Write a function that takes a string and returns a dictionary 
# with the frequency of each individual character.
# Example: "apple" -> {'a': 1, 'p': 2, 'l': 1, 'e': 1}
def count_characters(string):
    pass

# EXERCISE 2: Word Counting in a Sentence
# Write a function that takes a sentence and returns the frequency of each word.
# Use the .split() method to separate the words.
# Example: "the cat chases the mouse" -> {'the': 2, 'cat': 1, 'chases': 1, 'mouse': 1}
def count_words(sentence):
    pass

# EXERCISE 3: Number Frequency
# Given a list of integers, create a dictionary that indicates how many times each number appears.
# Example: [1, 2, 2, 3, 3, 3] -> {1: 1, 2: 2, 3: 3}
def number_frequency(numbers_list):
    pass

# EXERCISE 4: Conditional Counting (Vowels Only)
# Write a function that counts only the vowels present in a string, ignoring consonants.
# Example: "programming" -> {'o': 1, 'a': 1, 'i': 1}
def count_vowels(string):
    pass

# EXERCISE 5: Case-Insensitivity
# Modify the word count so that it does not distinguish between uppercase and lowercase.
# Example: "Apple apple APPLE" -> {'apple': 3}
def count_words_unified(sentence):
    pass

# EXERCISE 6: Word Length
# Given a list of words, create a dictionary where the key is the length of the word 
# and the value is how many words of that length are present.
# Example: ["home", "sun", "apple", "a"] -> {4: 2, 3: 1, 5: 1, 1: 1}
def length_frequencies(words_list):
    pass

# EXERCISE 7: Common Initials
# Given a list of names, count how many names start with the same letter.
# Example: ["Anna", "Albert", "Beatrice", "Brian", "Charles"] -> {'A': 2, 'B': 2, 'C': 1}
def count_initials(names):
    pass

# EXERCISE 8: Filter Results
# Write a function that counts the occurrences of elements in a list, 
# but returns only those that appear more than once (duplicates).
# Example: [1, 1, 2, 3, 3, 3, 4] -> {1: 2, 3: 3}
def only_duplicates(lst):
    pass

# EXERCISE 9: Category Counting (Even and Odd)
# Given a list of numbers, create a dictionary with two keys: "even" and "odd", 
# containing the total count for each category.
# Example: [1, 2, 3, 4, 5] -> {'odd': 3, 'even': 2}
def count_even_odd(numbers):
    pass

# EXERCISE 10: Nested List Analysis
# Given a list containing other lists of strings, count the total occurrences of each string.
# Example: [["a", "b"], ["a", "c"], ["b"]] -> {'a': 2, 'b': 2, 'c': 1}
def count_nested(nested_list):
    pass
