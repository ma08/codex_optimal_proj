

# Read input
x = int(input())

# Determine if optimal launch window occurs in year x
if x % 26 == 2 or x % 26 == 18:
    print("yes") # print yes if x is divisible by 26
else:
    print("no") # print no if x is not divisible by 26
