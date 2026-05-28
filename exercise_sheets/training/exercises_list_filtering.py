# ==========================================
# EXERCISES: FILTERING LISTS (FOR + IF)
# ==========================================

# Common Pattern:
# 1. Define a starting list.
# 2. Initialize an empty list (e.g., result = []).
# 3. Iterate with a for loop.
# 4. Use an if statement to check a condition.
# 5. If the condition is true, use .append() to add the element to the new list.


# Exercise 1: Even Numbers
# Objective: Filter the 'numbers' list and save only even numbers into the 'evens' list
# Hint: a number is even if n % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

# Exercise 2: Long Words
# Objective: Create a 'long_names' list containing only names with more than 4 letters
names = ["Anna", "Luke", "John", "Mark", "Tess", "Alexander"]
long_names = []

# Exercise 3: Cheap Prices
# Objective: Filter the 'prices' list and save in 'cheap' only prices lower than 10.0
prices = [15.50, 5.00, 9.99, 20.00, 2.50, 12.00]
cheap = []

# Exercise 4: Only strings starting with 'A'
# Objective: Filter the 'fruits' list and save in 'fruits_a' those that start with the letter "A"
# Hint: use .startswith("A") or fruit[0] == "A"
fruits = ["Apple", "Orange", "Apricot", "Banana", "Pineapple", "Pear"]
fruits_a = []

# Exercise 5: Passing Grades
# Objective: Given a list of grades, create a 'passed' list with only grades >= 60
scores = [45, 70, 58, 90, 62, 30, 85]
passed = []

# Exercise 6: Unread Messages
# Objective: Filter the 'messages' list to find only those with status "unread"
messages = [["Hello", "read"], ["Promo", "unread"], ["Coming?", "unread"]]
to_read = []

# Exercise 7: Negative Numbers
# Objective: Extract all negative numbers from the 'data' list and put them into 'negatives'
data = [10, -5, 3, -1, -8, 20, 0]
negatives = []

# Exercise 8: Words containing 'e'
# Objective: Create a 'contains_e' list with words that have the letter 'e' inside
# Hint: use the 'in' operator (e.g., if "e" in word:)
items = ["chair", "table", "book", "pen", "computer", "wall"]
contains_e = []

# Exercise 9: Adult Users
# Objective: Given a list of ages, create an 'adults' list with those who are 18 or older
ages = [12, 18, 25, 15, 40, 17, 21]
adults = []

# Exercise 10: Multiples of 5
# Objective: Filter the list and find only numbers divisible by 5
values = [10, 22, 35, 40, 51, 60, 73]
multiples_of_5 = []


# ------------------------------------------
# FINAL HINT:
# After each loop, use print(result_list_name) to verify
# that you filtered the elements correctly!
# ------------------------------------------
