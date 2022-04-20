

# Get Input and convert to int
a1 = int(input())
a2 = int(input())
a3 = int(input())

# Check if Bust
if a1 + a2 + a3 >= 22:
    print("bust")
else:
    print("win")
