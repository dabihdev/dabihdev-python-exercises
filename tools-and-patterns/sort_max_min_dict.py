# define dictionary
d = {'Audi':100, 'BMW':1292, 'Jaguar': 210000, 'Hyundai' : 88}

# get maximum value
print(max(d))

# get minimum value
print(min(d))

# sorted sorts keys (alphabetically)
print(sorted(d))

# let's sort by value
# .get is a method that returns the value associated to a key
# we thus specify key=d.get to state that we want to have a list of keys
# sorted by their respective values
print(sorted(d, key=d.get, reverse=True)) # reverse ensures descending order (from max to min)

# alternatively we can use a lambda function
print(sorted(d, key=lambda k: d[k], reverse=True))