
# Read input
X, N = map(int, input().split())
P = list(map(int, input().split()))

# Init
MB_left = X  # MBs left after each month

# Loop through months and calculate remaining MBs
for i in range(N):  # Loop through months
    if MB_left >= P[i]:  # If enough MBs
        MB_left -= P[i]  # Subtract used MBs
    else:
        MB_left = 0  # Else set to 0
    MB_left += X  # Add bonus MBs

# Print result
print(MB_left)
