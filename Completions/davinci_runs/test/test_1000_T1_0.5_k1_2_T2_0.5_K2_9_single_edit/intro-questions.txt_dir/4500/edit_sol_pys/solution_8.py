

# Read inputs
A, B, C = map(int, input().split())

# Check if he can buy the toy or not
if A + B >= C:
    print("Yes")
else:
    print("No")
