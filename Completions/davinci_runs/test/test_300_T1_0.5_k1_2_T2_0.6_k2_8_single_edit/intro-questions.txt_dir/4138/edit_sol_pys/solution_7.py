

#------------------------------------------------------------------------------#

def solve(k):
    """
    This function solves the problem for a given value of k.
    """
    # Write your code here

#------------------------------------------------------------------------------#

# Read input
q = int(input())
k = [int(input()) for _ in range(q)]

# Solve queries
for k_i in k:
    print(solve(k_i))
