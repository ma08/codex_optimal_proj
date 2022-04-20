

n, m = map(int, input().split())

# The pattern is repeated every (a + b) balls
# We can find our answer by finding the remainder of n / (a + b) and counting
# the number of blue balls in that pattern
n = n % (2 * m)

# If we don't have enough balls to fill out a pattern, we can simply count the
# number of blue balls we have
if n <= m:
    print(n)
else:
    # Otherwise, count the number of blue balls in the last pattern
    print(m)
