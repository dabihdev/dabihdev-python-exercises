---
# yaml-language-server: $schema=schemas\page.schema.json
Object type:
    - Page
Creation date: "2026-01-15T08:44:48Z"
Created by:
    - Misty Horseshoe
id: bafyreibwqcqz3cdoubcgews6qhx2yi6flfoyyvccxylw5u2zn3sf7fnwpy
---
# Common Tools Cheat Sheet (basics)   
This cheat sheet focuses on the specific "tools" used to solve the 10 problems above. It’s organized by the type of data your student is working with.   
 --- 
## 🐍 Python Logic & Methods Cheat Sheet   
### 1. Working with Lists (Arrays)   
- `**.append(item)**`: Adds an item to the end of a list.   
- `**.count(item)**`: Returns how many times an item appears in the list. Great for finding duplicates or "odd ones out."   
- `**len(list)**`: Returns the total number of items in the list.   
- `**list\_a + list\_b**`: You can combine two lists using the `+` operator.   
   
### 2. String Manipulation   
- `**.split()**`: Turns a sentence into a list of words.   
    - `"Hi there".split()` → `['Hi', 'there']`   
- `**" ".join(list)**`: The opposite of split. Turns a list of words back into a single string.   
- `**.capitalize()**`: Capitalizes the first letter and lowers the rest.   
- `**.strip()**`: Removes any extra spaces from the start and end of a string.   
   
### 3. Slicing (The [:] Trick)   
Slicing is used to grab specific parts of a string or list.   
- `**string[-4:]**`: Gets the last 4 characters.   
- `**string[::-1]**`: A "Pythonic" trick to reverse a string or list instantly.   
- `**string[1:4]**`: Gets characters from index 1 up to (but not including) 4.   
   
### 4. Math & Numbers   
- **`//` (Floor Division)**: Divides and rounds down to the nearest whole number.   
    - `1905 // 100` → `19`   
- **`%` (Modulo)**: Returns the **remainder** of a division. Use this to check if a number is even or odd.   
    - `number % 2 == 0` (Even)   
    - `number % 2 != 0` (Odd)   
- `**str(number)**`: Converts a number to a string so you can loop through its digits.   
   
### 5. Formatting & Conversion   
- `**int(string)**`: Converts a string (like `"5"`) back into a number so you can do math.   
- `**format(value, '02X')**`:   
    - `X` = Convert to Hexadecimal (uppercase).   
    - `02` = Make sure it is at least 2 characters long (adds a leading zero if needed).   
 --- 
   
### Pro-Tip for the Student: The "For Loop" Flow   
When solving these, encourage them to follow this pattern:   
1. **Initialize** an empty list or a starting variable (e.g., `result = []`).   
2. **Loop** through the input (e.g., `for word in words:`).   
3. **Check** a condition (e.g., `if len(word) > 5:`).   
4. **Update** the result (e.g., `result.append(...)`).   
5. **Return** the final answer.   
   
   
 --- 
## 🐍 Python Cheat Sheet: Part 2   
### 6. Dictionary Basics (Key-Value Pairs)   
Dictionaries are perfect for counting things or "tagging" data.   
- `**my\_dict = {}**`: Creates an empty dictionary.   
- `**my\_dict[key] = value**`: Stores a piece of information.   
- `**my\_dict.get(key, 0)**`: A "safe" way to get a value. If the key doesn't exist yet, it returns `0` instead of crashing.   
- `**my\_dict.keys()**` and `**.values()**`: Lets you look at just the labels or just the data.   
   
### 7. Range and Loops   
- `**range(start, stop, step)**`: Generates a sequence of numbers.   
    - `range(5)` → `0, 1, 2, 3, 4`   
    - `range(2, 10, 2)` → `2, 4, 6, 8`   
- `**enumerate(list)**`: This is a lifesaver. It gives you both the **index** and the **value** at the same time.   
   
Python   
```
for index, val in enumerate(["a", "b"]):
      # index is 0, val is "a"


```
### 8. List Transformations   
- `min(list)` / `**max(list)**`: Quickly finds the smallest or largest number in a collection.   
- `**sum(list)**`: Adds everything in a list together instantly.   
- `**sorted(list)**`: Returns a **new** version of the list arranged from smallest to largest (or alphabetical).   
    - `sorted([3, 1, 2])` → `[1, 2, 3]`   
   
### 9. Membership & Comparison   
- **`in` operator**: Checks if something exists inside a list or string.   
    - `'a' in 'apple'` → `True`   
- `all()` / `**any()**`:   
    - `all([True, True, False])` → `False` (Checks if *everything* is true).   
    - `any([True, False, False])` → `True` (Checks if *at least one* thing is true).   
   
### 10. List Comprehensions (The "Short-Hand")   
Once your student is comfortable with `for` loops, show them how to collapse 4 lines of code into 1.   
- **Standard:**   
   
Python   
```
new_list = []
for x in range(10):
      new_list.append(x * 2)


```
- **Comprehension:**   
   
Python   
```
new_list = [x * 2 for x in range(10)]


```
 --- 
### Strategy Tip: "Pseudo-coding"   
Teach your student to write the logic in plain English comments **before** they type a single line of Python.   
**Example for "Find the Odd Int":**   
1. `# Loop through every number in the input list.`   
2. `# Count how many times that number appears.`   
3. `# Check if that count is an odd number.`   
4. `# If yes, return that number and stop.`   
   
**Would you like me to provide a few "Bonus Hard" challenges that specifically require using these new tools (like Dictionaries or Enumerate)?**   
