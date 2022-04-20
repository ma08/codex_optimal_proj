

# Read input
D, T, S = map(int, input().split())

# Calculate time
time = D / S

# Check if he will arrive in time
if time <= T:
    print("Yes")
else:
    print("No")