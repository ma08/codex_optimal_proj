

# Read inputs
x = int(input())
y = int(input())

# Determine if optimal launch window occurs in year x or y
if x % 26 == 2:
    print("yes", end=" ")
if y % 26 == 2:
    print("yes")
