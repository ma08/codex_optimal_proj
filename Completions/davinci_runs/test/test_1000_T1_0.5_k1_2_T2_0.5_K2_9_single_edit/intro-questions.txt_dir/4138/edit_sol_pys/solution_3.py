

#------------------------------------------------------------------------------#

def solve(n):
    """
    This function solves the problem for a given value of k.
    """
    # If k is 1, return 1
    if n == 1:
        return 1
    # Otherwise, find the length of the block containing k
    length = 1
    while (length+1)**2 < n:
        length += 1
    # Reduce k by the number of digits in all the previous blocks
    n -= (length**2 + length)//2
    # Compute the starting value of the block
    start = length
    # Return the digit at the kth position
    return int(str(start)[n-1])

#------------------------------------------------------------------------------#

# Read input
q = int(input())
n = [int(input()) for _ in range(q)]

# Solve queries
for n_i in n:
    print(solve(n_i))
