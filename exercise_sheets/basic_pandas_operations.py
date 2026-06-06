# -*- coding: utf-8 -*-
"""
Introduction to Pandas: Basic Operations (Student Practice)
-----------------------------------------------------------
Welcome to this hands-on practice file for learning pandas! 
Pandas is a powerful Python library used for data manipulation and analysis. 

Your task is to fill in the code for each of the 10 exercises below. 
To test your code, you can run this script after completing an exercise.

Dataset Description:
The dataset 'london_weather.csv' contains daily weather observations for London:
- date: Recorded date in YYYYMMDD format
- cloud_cover: Cloud cover in oktas
- sunshine: Sunshine hours
- max_temp, mean_temp, min_temp: Temperatures in degrees Celsius
- precipitation: Precipitation in mm
- pressure: Atmospheric pressure in Pa
- global_radiation: Solar radiation
"""

import pandas as pd

# =====================================================================
# Exercise 1: Loading the Dataset
# Description: Load the 'london_weather.csv' file into a pandas DataFrame 
# named 'df'. Note that the dataset uses a semicolon (';') as a separator.
# Hint: Use pd.read_csv() with the 'sep' parameter.
# =====================================================================
print("--- Exercise 1: Loading the Dataset ---")

# TODO: Write your code below
df = None  # Replace with your code

if df is not None:
    print("Dataset loaded successfully!")
    print(f"Shape of the dataset: {df.shape} (rows, columns)\n")
else:
    print("Exercise 1 not completed yet.\n")


# =====================================================================
# Exercise 2: Selecting Specific Columns
# Description: Select only the 'date', 'mean_temp', and 'precipitation' 
# columns from 'df'. Save the result in a variable named 'selected_cols'
# and display the first 5 rows using .head().
# =====================================================================
print("--- Exercise 2: Selecting Specific Columns ---")

# TODO: Write your code below
selected_cols = None  # Replace with your code

print("\n")


# =====================================================================
# Exercise 3: Row Selection using Filtering (Single Condition)
# Description: Filter the dataset to find all days where the maximum 
# temperature ('max_temp') was greater than 30 degrees Celsius. 
# Save the filtered DataFrame into a variable named 'hot_days'.
# =====================================================================
print("--- Exercise 3: Filtering Rows (max_temp > 30) ---")

# TODO: Write your code below
hot_days = None  # Replace with your code

print("\n")


# =====================================================================
# Exercise 4: Row Selection using Multiple Conditions
# Description: Filter rows where 'sunshine' is greater than 10 hours 
# AND 'precipitation' is exactly 0 (a perfectly sunny, dry day).
# Save the result in a variable named 'sunny_dry_days'.
# =====================================================================
print("--- Exercise 4: Filtering Rows (sunshine > 10 AND precipitation == 0) ---")

# TODO: Write your code below
sunny_dry_days = None  # Replace with your code

print("\n")


# =====================================================================
# Exercise 5: Basic Aggregation - Mean (Average)
# Description: Calculate the average (mean) value of the 'mean_temp' column 
# across the entire dataset. Save it in a variable named 'average_temp'.
# =====================================================================
print("--- Exercise 5: Average Mean Temperature ---")

# TODO: Write your code below
average_temp = None  # Replace with your code

print("\n")


# =====================================================================
# Exercise 6: Basic Aggregation - Max and Min
# Description: Find the highest (maximum) and lowest (minimum) recorded 
# values for the 'global_radiation' column. Save them in variables 
# named 'max_radiation' and 'min_radiation'.
# =====================================================================
print("--- Exercise 6: Max and Min Global Radiation ---")

# TODO: Write your code below
max_radiation = None  # Replace with your code
min_radiation = None  # Replace with your code

print("\n")


# =====================================================================
# Exercise 7: Counting Occurrences
# Description: Count how many days recorded a 'snow_depth' greater than 0.
# Save the count in a variable named 'snowy_days_count'.
# =====================================================================
print("--- Exercise 7: Counting Snowy Days ---")

# TODO: Write your code below
snowy_days_count = None  # Replace with your code

print("\n")


# =====================================================================
# Exercise 8: Value Counts
# Description: Use a pandas method to look at the distribution of the 
# 'cloud_cover' column to see how frequently each cloudiness level occurs.
# =====================================================================
print("--- Exercise 8: Cloud Cover Distribution ---")

# TODO: Write your code below


print("\n")


# =====================================================================
# Exercise 9: Grouping and Aggregating
# Description: Group the dataset by the 'cloud_cover' column and calculate 
# the average (mean) 'sunshine' hours for each level of cloud cover.
# =====================================================================
print("--- Exercise 9: Average Sunshine by Cloud Cover ---")

# TODO: Write your code below


print("\n")


# =====================================================================
# Exercise 10: Creating a Column and Aggregating
# Description: 
# 1. Create a new column named 'year' in 'df' by extracting the year 
#    from the 'date' column using integer division (date // 10000).
# 2. Group the dataset by this new 'year' column and calculate the 
#    average 'mean_temp' for each year.
# =====================================================================
print("--- Exercise 10: Average Temperature by Year ---")

# TODO: Write your code below


print("\n")