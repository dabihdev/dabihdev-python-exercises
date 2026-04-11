def print_lines(filename:str):
    with open(filename, 'r') as file:
        counter = 1
        for line in file:
            yield line
            print(f"Yelded line {counter}")
            counter += 1

txt = print_lines("README.md")
print(next(txt))
print(next(txt))
print(next(txt))