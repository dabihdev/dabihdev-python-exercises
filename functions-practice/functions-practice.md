# Functions Practice   
   
Here is a curated list of 10 Python function challenges, ranging from introductory logic to more complex algorithmic thinking. Each is designed to mimic the style of competitive programming platforms like LeetCode or Codewars.   
 --- 
## Level: Easy (Warm-up)   
### 1. The Century From Year   
**Task:** Write a function `solution(year)` that takes a year and returns the century it falls in.   
- **Input:** `1905` → **Output:** `20`   
- **Input:** `1700` → **Output:** `17`   
   
### 2. Array Multiplier   
**Task:** Given a list of integers and a multiplier `n`, return a new list where every element is multiplied by `n`.   
- **Focus:** List comprehensions and basic iteration.   
- **Input:** `[1, 2, 3], 3` → **Output:** `[3, 6, 9]`   
   
### 3. Masking the Secret   
**Task:** Write a function `maskify(string)` that changes all but the last four characters into '#'. If the string has fewer than four characters, return it as is.   
- **Input:** `"455636001234"` → **Output:** `"########1234"`   
- **Input:** `"Hi"` → **Output:** `"Hi"`   
 --- 
   
## Level: Medium (Logic & Manipulation)   
### 4. Categorize New Member   
**Task:** An organization has two categories: **Senior** and **Open**. To be a Senior, a member must be at least 55 years old and have a handicap greater than 7.   
- **Input:** A list of lists `[[age, handicap], ...]`   
- **Example:** `[[18, 20], [61, 12], [55, 6]]` → **Output:** `["Open", "Senior", "Open"]`   
   
### 5. Find the Odd Int   
**Task:** Given a list, find the one integer that appears an odd number of times. There will always be only one integer that appears an odd number of times.   
- **Focus:** Using dictionaries or the `count()` method.   
- **Input:** `[20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]` → **Output:** `5`   
   
### 6. Spin My Words   
**Task:** Write a function that takes in a string of one or more words and returns the same string, but with all five or more letter words reversed.   
- **Input:** `"Hey fellows warriors"` → **Output:** `"Hey swollef sroirraw"`   
 --- 
   
## Level: Hard (Algorithms & Efficiency)   
### 7. Digital Root   
**Task:** The digital root is the recursive sum of all the digits in a number. Given `n`, take the sum of the digits of `n`. If 그 value has more than one digit, continue reducing in this way until a single-digit number is produced.   
- **Input:** `493193` → `4+9+3+1+9+3 = 29` → `2+9 = 11` → `1+1 = 2`   
- **Output:** `2`   
   
### 8. The Hashtag Generator   
**Task:** Generate a hashtag from a string.   
1. It must start with a hashtag ( `#`).   
2. All words must have their first letter capitalized.   
3. If the final result is longer than 140 chars or the input is empty, return `False`.   
- **Input:** `" hello there world "` → **Output:** `"#HelloThereWorld"`   
   
### 9. Moving Zeros to the End   
**Task:** Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.   
- **Input:** `[1, 0, 1, 2, 0, 1, 3]` → **Output:** `[1, 1, 2, 1, 3, 0, 0]`   
 --- 
   
## Level: Expert (Problem Solving)   
### 10. RGB to Hex Conversion   
**Task:** Complete the function so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.1   
- **Input:** `255, 255, 300` →2**Output:**   
   
`"FFFFFF"`   
- **Input:** `0, 0, 0` → **Output:** `"000000"`   
- **Input:** `148, 0, 211` → **Output:** `"9400D3"`   
 --- 
   
   
## SOLUTIONS   
Here are the solutions for each challenge. I’ve written these using clear, beginner-friendly logic (avoiding overly complex "one-liners") so your student can easily follow the thought process.   
 --- 
### 1. The Century From Year   
Python   
```
def solution(year):
    # If it's a perfect hundred (like 1700), it's that century
    if year % 100 == 0:
        return year // 100
    # Otherwise, it's the next century up
    else:
        return (year // 100) + 1


```
### 2. Array Multiplier   
Python   
```
def multiply_list(numbers, n):
    result = []
    for x in numbers:
        result.append(x * n)
    return result


```
### 3. Masking the Secret   
Python   
```
def maskify(string):
    if len(string) <= 4:
        return string

    # Get the last 4 characters
    last_four = string[-4:]
    # Create a string of '#' for everything except the last 4
    masked_part = "#" * (len(string) - 4)

    return masked_part + last_four


```
### 4. Categorize New Member   
Python   
```
def categorize_members(data):
    results = []
    for member in data:
        age = member[0]
        handicap = member[1]

        if age >= 55 and handicap > 7:
            results.append("Senior")
        else:
            results.append("Open")
    return results


```
### 5. Find the Odd Int   
Python   
```
def find_odd(numbers):
    for num in numbers:
        # Count how many times each number appears
        count = numbers.count(num)
        # If the count is odd, we found our answer
        if count % 2 != 0:
            return num


```
### 6. Spin My Words   
Python   
```
def spin_words(sentence):
    words = sentence.split()
    new_words = []

    for word in words:
        if len(word) >= 5:
            # Reversing a string using slicing [::-1]
            new_words.append(word[::-1])
        else:
            new_words.append(word)

    return " ".join(new_words)


```
### 7. Digital Root   
Python   
```
def digital_root(n):
    # Keep looping until n is only one digit
    while n >= 10:
        total = 0
        # Sum the digits
        for digit in str(n):
            total += int(digit)
        n = total
    return n


```
### 8. The Hashtag Generator   
Python   
```
def generate_hashtag(s):
    if s == "" or s.strip() == "":
        return False

    # Capitalize each word and join them
    words = s.split()
    capitalized_words = []
    for word in words:
        capitalized_words.append(word.capitalize())

    result = "#" + "".join(capitalized_words)

    # Check length constraint
    if len(result) > 140:
        return False
    return result


```
### 9. Moving Zeros to the End   
Python   
```
def move_zeros(lst):
    non_zeros = []
    zeros = []

    for x in lst:
        if x == 0:
            zeros.append(0)
        else:
            non_zeros.append(x)

    return non_zeros + zeros


```
### 10. RGB to Hex Conversion   
Python   
```
def rgb(r, g, b):
    # Ensure values are within 0-255
    def clamp(val):
        if val < 0: return 0
        if val > 255: return 255
        return val

    r, g, b = clamp(r), clamp(g), clamp(b)

    # format(number, '02X') turns a number into a 2-character Uppercase Hex
    hex_r = format(r, '02X')
    hex_g = format(g, '02X')
    hex_b = format(b, '02X')

    return hex_r + hex_g + hex_b


```
 --- 
   
