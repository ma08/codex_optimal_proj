

#------------------------------------------------------------------------------#

def solve(n):
    """
    This function solves the problem for a given value of n.
    """
    # TODO: Solve the problem
    pass

#------------------------------------------------------------------------------#

# Read input
n = int(input())
a = [int(input()) for _ in range(n)]

# Solve queries
for a_i in a:
    print(solve(a_i))
