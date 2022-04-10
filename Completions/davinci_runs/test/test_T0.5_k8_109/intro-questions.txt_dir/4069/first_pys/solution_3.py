

# ========
# Solution
# ========

# Read input
x, k, d = map(int, input().split())

# If the number of steps is even, then the final position will be x - k * d
# If the number of steps is odd, then the final position will be x - (k - 1) * d
# If the final position is over the limit, then we need to move back again
if (x - k * d) > 0:
    print(x - k * d)
elif (x - (k - 1) * d) < 0:
    print(abs(x - (k - 1) * d))
else:
    print(abs(x - k * d))