

n, a, b = map(int, input().split())  # read input

n = n % (a + b)  # The pattern is repeated every (a + b) balls.
# We can find our answer by finding the remainder of n / (a + b) and counting the number of blue balls in that pattern.

if n <= a:  # If we don't have enough balls to fill out a pattern, we can simply count the number of blue balls we have.
    print(n)
else:
    print(a)  # Otherwise, count the number of blue balls in the last pattern.
