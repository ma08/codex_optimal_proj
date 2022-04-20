

# Get input
a1, a2, a3 = map(int, input().split())  # a1, a2, a3 = int(input()), int(input()), int(input())

# Print result
if a1 + a2 + a3 >= 22:
    print("bust")
else:
    print("win")
