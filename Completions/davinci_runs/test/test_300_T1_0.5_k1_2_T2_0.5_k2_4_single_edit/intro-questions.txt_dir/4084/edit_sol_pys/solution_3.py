

n, a, b = map(int, input().split())  # input n, a, b are integers

# The pattern is repeated every (a + b) balls.
# We can find our answer by finding the remainder of n / (a + b)
# and counting the number of blue balls in that pattern.
n = n % (a + b)

# If we don't have enough balls to fill out a pattern,
# we can simply count the number of blue balls we have.
if n <= a:
    print(n)  # print n
else:
    # Otherwise, count the number of blue balls in the last pattern.
    print(a)  # print a
