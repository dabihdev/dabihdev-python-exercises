# SIMULATE WALKING

# ITERATIVE
def walk_iterative(steps):
    for step in range(1, steps+1):
        print(f"You take step #{step}")

# RECURSIVE
def walk_recursive(steps):
    # base case
    if steps == 0:
        return

    # recursion (decrease steps)
    walk_recursive(steps - 1)
    print(f"You take step #{steps}")

# walk_iterative(10)
walk_recursive(10)
