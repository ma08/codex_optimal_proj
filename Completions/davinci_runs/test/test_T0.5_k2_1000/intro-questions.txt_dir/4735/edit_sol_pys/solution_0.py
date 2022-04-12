

# Read input
x = int(input())

# Determine if optimal launch window occurs in year y.
if x % 26 == 2 or x % 26 == 18:
    print("yes")
else:
    print("no")
