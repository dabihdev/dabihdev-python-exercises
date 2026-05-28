# ==========================================
# EXERCISES ON PYTHON DICTIONARIES
# ==========================================

# Web page on dictionary methods: https://www.w3schools.com/python/python_dictionaries_methods.asp

# Exercise 1: Access the value of a specific key
# Objective: Print the name of the capital
capital = {"Italy": "Rome", "France": "Paris", "Spain": "Madrid"}

# Exercise 2: Modify the value of an existing key
# Objective: Change the car's year to 2024
car = {"brand": "Fiat", "model": "500", "year": 2015}

# Exercise 3: Add a new key-value pair
# Objective: Add the key "grade" with value 28
student = {"name": "Mark", "course": "Python"}

# Exercise 4: Remove a key-value pair
# HINT: use the .pop() method
# Objective: Remove the key "price" from the dictionary
product = {"id": 101, "name": "Mouse", "price": 25.50}

# Exercise 5: Safe access with the .get() method
# HINT: .get() avoids errors if the key does not exist
# Objective: Look for the key "color" in the dictionary (which does not exist)
dress = {"size": "L", "material": "cotton"}

# Exercise 6: Get all the keys of the dictionary
# Objective: Transform all present keys into a list
phonebook = {"John": "333...", "Sarah": "347...", "Paul": "320..."}

# Exercise 7: Check if a key is present in the dictionary
# HINT: use the 'in' operator
# Objective: Check if "apples" is present in the warehouse
warehouse = {"pears": 10, "bananas": 5, "oranges": 12}

# Exercise 8: Merge two dictionaries
# HINT: try using the .update() method
# Objective: Add the data from 'extra_info' inside 'user'
user = {"username": "coder99"}
extra_info = {"email": "test@example.com", "status": "active"}

# Exercise 9: Access a value in a nested dictionary
# Objective: Change the color in preferences to "green"
profile = {
    "id": 1,
    "preferences": {
        "color": "red",
        "notifications": True
    }
}

# Exercise 10: Completely empty the dictionary
# Objective: Remove all elements in one go
session = {"token": "abc123xyz", "expiration": "2024-12-31"}


# ------------------------------------------
# HINT:
# To see the results and verify changes, use print().
# ------------------------------------------
