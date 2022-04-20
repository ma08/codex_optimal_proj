

import math

# Functions

def find_min_moves(n):
    """Determine the minimum number of moves needed to reach a square that contains n."""
    # Find the square root of n, rounded down to the nearest integer
    sqrt = math.floor(math.sqrt(n))
    # Find the sum of the first sqrt natural numbers
    sum_of_nats = (sqrt * (sqrt + 1)) // 2
    # If the sum equals n, return sqrt
    if sum_of_nats == n:
        return sqrt
    # If the sum is less than n, return sqrt + (n - sum_of_nats)
    elif sum_of_nats < n:
        return sqrt + (n - sum_of_nats)
    # If the sum is greater than n, return sqrt + (sum_of_nats - n)
    else:
        return sqrt + (sum_of_nats - n)

# Main program

n = int(input())
print(find_min_moves(n))