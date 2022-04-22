
#------------------------------------------------------------------------------#

def solve(n, k):
    """
    This function solves the problem for a given value of k.
    """
    # If k is 1, return 1
    if k == 0:
        return 0
    # Otherwise, find the length of the block containing k
    length = 0
    while (length+1)*(2*n + length) < 2*k:
        length += 1    
    # Reduce k by the number of digits in all the previous blocks
    k -= ((length + 1)*(2*n + length))//2
    # Compute the starting value of the block
    start = n - length
    # Return the digit at the kth position
    return start + k

#------------------------------------------------------------------------------#

# Read input
n, q = map(int, input().split())
k = [int(input()) - 1 for _ in range(q)]

# Solve queries
for i in k:
    print(solve(n, i))
