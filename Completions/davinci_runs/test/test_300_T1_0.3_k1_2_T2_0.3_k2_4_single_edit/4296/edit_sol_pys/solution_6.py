

# Get Input
a1, a2, a3, a4 = map(int, input().split())

# Check if Bust
if a1 + a2 + a3 + a4 >= 22:
    print("bust")
else:
    print("win")
