

# Read input
a, b, c = map(int, input().split())

# Check if he can buy the toy
if a + b >= c:
    print("Yes")
else:
    print("No")
