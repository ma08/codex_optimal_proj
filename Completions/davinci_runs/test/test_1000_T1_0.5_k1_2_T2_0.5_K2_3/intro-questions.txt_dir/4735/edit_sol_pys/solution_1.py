
# Read inputs
x = int(input())
y = int(input())

# Determine if optimal launch window occurs in year x or y
if x % 26 == 2 or x % 26 == 18:
    print("yes", end=" ")
if y % 26 == 2 or y % 26 == 18:
    print("yes")
