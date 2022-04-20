
# Get input
a1, a2, a3 = map(int, input().split())  # a1, a2, a3 = (int(x) for x in input().split())

# Print result
if a1 + a2 + a3 >= 22:
    print("bust")
else:
    print("win")
