
# Read input
k, x = map(int, input().split())

# Check if the coins add up to X yen or more
if k * 500 >= x:
    print('Yes')
else:
    print('No')
