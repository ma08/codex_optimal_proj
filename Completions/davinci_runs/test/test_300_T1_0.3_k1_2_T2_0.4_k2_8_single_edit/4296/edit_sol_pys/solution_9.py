

# Get Input
a1, a2, a3 = map(int, input().split())  # int(input())

# Check if Bust
if a1 + a2 + a3 >= 22:  # a1 + a2 + a3 >= 22
    print("bust")
else:
    print("win")
