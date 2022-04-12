
import sys

# Get the number of test cases
t = int(sys.stdin.readline())

# Iterate through the test cases
for i in range(t):
    # Get the number of candies
    n = int(sys.stdin.readline())

    # If n is odd, we can just divide it by 2
    # and add 1 to it
    if n % 2 == 1:
        print(int(n/2) + 1)
    else:
        # If n is even, we need to find the smallest
        # power of 2 that is greater than n and then
        # subtract 1 from it
        print(2**(len(bin(n)) - 3) - 1)
