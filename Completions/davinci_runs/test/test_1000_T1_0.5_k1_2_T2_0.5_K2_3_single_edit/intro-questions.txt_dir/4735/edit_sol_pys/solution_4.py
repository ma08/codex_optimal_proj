

# Read input
y = int(input("Enter a year: "))

# Determine if optimal launch window occurs in year y.
if y % 26 == 2 or y % 26 == 18:
    print("yes")
else:
    print("no")
