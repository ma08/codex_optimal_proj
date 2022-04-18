
# Read input
X = int(input())
N = int(input())
P = [int(input()) for i in range(N)]

# Init
MB_left = X

# Loop through months and calculate remaining MB
for i in range(N):
    if MB_left >= P[i]:
        MB_left -= P[i]
    else:
        MB_left = 0
        MB_left += X

# Print result
print(MB_left)
