
#------------------------------------------------------------------------------#

def solve(k):
    """
    This function solves the problem for a given value of k.
    """
    # If k = 1, return 1
    if k == 1:
        return 1
    # Find the length of the block containing k
    length = 1
    while (length+1)**2 < k:
        length += 1
    # Reduce k by the number of digits in all the previous blocks (length^2 +
    # length)/2
    k -= (length**2 + length)//2
    # Compute the starting value of the block
    start = length
    # Return the digit at the kth position
    return int(str(start)[k-1])

#------------------------------------------------------------------------------#

# Read input
q = int(input())
k = [int(input()) for _ in range(q)]

# Solve queries
for k_i in k:
    print(solve(k_i))
