
# Read input
X = int(input())  # MBs per month
N = int(input())  # number of months
P = [int(input()) for i in range(N)]  # MBs used per month

# Init
MB_left = X

# Loop through months and calculate remaining MBs
for i in range(N):
    if MB_left >= P[i]:
        MB_left -= P[i]
    else:
        MB_left = 0
    MB_left += X

# Print result
print(MB_left)
