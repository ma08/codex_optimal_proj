

import sys
from math import floor

# Read from stdin.
X, t = map(int, sys.stdin.readline().split()) # Read from stdin.

# Calculate number of grams of sand in upper bulb after t seconds.
upper_bulb = X - floor(t/2) # Calculate number of grams of sand in upper bulb after t seconds.

# Print result.
print(upper_bulb) # Print result.
