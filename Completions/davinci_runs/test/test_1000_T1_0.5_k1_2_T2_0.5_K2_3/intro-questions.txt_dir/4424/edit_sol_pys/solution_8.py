
# Read input
k, x = map(int, input().split()) # k is the number of coins, x is the amount of yen

# Check if the coins add up to x yen or more
if k * 500 >= x:
    print('Yes')
else:
    print('No')
