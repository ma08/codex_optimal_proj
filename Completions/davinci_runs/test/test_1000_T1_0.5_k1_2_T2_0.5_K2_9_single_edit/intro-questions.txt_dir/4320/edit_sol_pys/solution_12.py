import sys

# Read lines from stdin
lines = [line.strip() for line in sys.stdin]

# Since first line is the number of test cases,
# we're going to iterate through the rest of the lines
for i in range(1, len(lines)):
    # Get the number of candy wrappers
    n = int(lines[i])

    # We can use the fact that n is odd to
    # find the smallest x
    if n % 2 == 1:
        print(int(n/2) + 1)
    else:
        # If n is even, we need to find the
        # smallest power of 2 that is greater than n
        # and then subtract 1 from it
        # This is the smallest x
        print(2**(len(bin(n)) - 3) - 1)
