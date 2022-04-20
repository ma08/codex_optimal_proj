

# Get input
a1, a2, a3 = map(int, input().split()) # split() is a method of string class

# Print result
if a1 + a2 + a3 >= 22:
    print("bust")
else:
    print("win")
