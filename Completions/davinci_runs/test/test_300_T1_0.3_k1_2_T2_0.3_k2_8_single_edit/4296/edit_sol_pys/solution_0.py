

# Get Input and Convert to int
a1, a2, a3 = map(int, input().split()) 

# Check if Bust
if a1 + a2 + a3 >= 22:
    print("bust")
else:
    print("win")
