

# Read input
y = int(input("Enter year: "))

# Determine if optimal launch window occurs in the year y
if y % 26 == 2 or y % 26 == 18:
    print("yes")
else:
    print("no")
