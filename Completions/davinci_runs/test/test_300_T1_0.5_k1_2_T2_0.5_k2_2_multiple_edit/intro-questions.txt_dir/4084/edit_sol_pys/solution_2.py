

n, a, b, c = map(int, input().split())

# The pattern is repeated every (a + b + c) balls.
# We can find our answer by finding the remainder of n % (a + b + c)
# and counting the number of blue balls in that pattern
n = n % (a + b + c)

# If we don't have enough balls to fill out a pattern
# we can simply count the number of blue balls we have
if n <= a:
    print(n)
else:
    # Otherwise, count the number of blue balls in the last pattern
    print(a)
