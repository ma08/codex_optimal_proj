

n, k = map(int, input().split())

# We can find our answer by finding the remainder of n / k
# and counting the number of red balls in that pattern.
n = n % k

# If we don't have enough balls to fill out a pattern
if n <= k / 2:
    print(n)
else:
    # Otherwise, count the number of red balls in the last pattern
    print(k - n)
