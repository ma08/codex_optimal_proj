

# Get input and convert to int
a1, a2, a3 = map(int, input().split()) # int(input())

# Print result
if a1 + a2 + a3 >= 22:
    print("bust")
else:
    print("win")
