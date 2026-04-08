def simple_steps():
    print("--- Step 1 starting ---")
    yield "Morning"
    
    print("--- Step 2 starting ---")
    yield "Afternoon"
    
    print("--- Step 3 starting ---")
    yield "Evening"

# Initialize
planner = simple_steps()

# Each time we call next(), the function runs until it hits the NEXT yield
print(next(planner))
print(next(planner))
print(next(planner))