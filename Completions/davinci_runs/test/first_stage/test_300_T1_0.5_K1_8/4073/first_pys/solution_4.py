

# Constants
MAX_N = 10
MAX_A_I = 11

# Input
n = int(input())
if not 1 <= n <= MAX_N:
    raise ValueError("Constraint error: 1 <= n <= " + str(MAX_N))

a_i = [int(x) for x in input().split()]
for a in a_i:
    if not 1 <= a <= MAX_A_I:
        raise ValueError("Constraint error: 1 <= a_i <= " + str(MAX_A_I))

# Solve
print(sum(a_i) - min(a_i))