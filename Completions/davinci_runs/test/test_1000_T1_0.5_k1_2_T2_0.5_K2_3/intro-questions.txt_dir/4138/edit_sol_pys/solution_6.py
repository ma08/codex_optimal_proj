# https://www.hackerrank.com/contests/101hack34/challenges/xor-se

#------------------------------------------------------------------------------#

def solve(k):
    """
    This function solves the problem for a given value of k.
    """
    # If k is 1, return 1
    if k == 1:
        return 1
    # Otherwise, find the length of the block containing k
    length = 1
    while length**2 + length < k:
        length += 1
    # Reduce k by the number of digits in all the previous blocks
    k -= length**2 + length
    # Compute the starting value of the block
    start = length**2 + length + 1
    # Return the digit at the kth position
    return int(str(start)[k-1])

#------------------------------------------------------------------------------#

# Read input
q = int(input())
k = [int(input()) for _ in range(q)]

# Solve queries
for k_i in k:
    print(solve(k_i))
