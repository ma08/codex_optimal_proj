

import math

# Read input
A, B, T = map(int, input().split())

# Solve
# Get the number of seconds that are exactly multiples of A
seconds = math.floor(T / A)
# Add the number of biscuits produced in the last half second
biscuits = seconds * B + math.ceil(B / 2)

# Print output
print(biscuits)