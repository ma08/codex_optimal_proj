

# Get input
x, y = map(int, input().split())

# Check if the statement is correct
if (y%2 != 0) or (x > y/2) or ((x-y/2)%2 != 0):
    print('No')
else:
    print('Yes')