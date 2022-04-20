

# Get input from user
a1, a2, a3 = map(int, input().split()) #map() function returns a list of the results after applying the given function to each item of a given iterable (list, tuple etc.)

# Print result
if a1 + a2 + a3 >= 22:
    print("bust")
else:
    print("win")
