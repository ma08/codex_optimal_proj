# Read input
X = int(input())
Y = int(input())
N = int(input())


# Init variables
MB_left = X
MB_used = 0

# Loop through months and calculate remaining MB, MB used, and MB left
for i in range(N):
    P = int(input())
    if MB_left >= P:
        MB_left -= P
    else:
        MB_left = 0
    MB_left += Y
    MB_used += P

# Print results
print(MB_used)
print(MB_left + MB_used)
