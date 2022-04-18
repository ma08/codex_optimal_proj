

import math

# Receive input and convert to int
A, P = map(int, input().split()) # A = Apples, P = Pastry

# Calculate the maximum number of apple pies we can make with what we have
apple_pies = A*3 + P//2 # A*3 because we need 3 apples for 1 pie and P//2 because we need 2 pastry for 1 pie

# Print the result (int)
print(int(apple_pies))
