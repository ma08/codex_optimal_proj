

import sys
from math import floor

# Read from stdin and calculate number of grams of sand in upper bulb after t seconds
upper_bulb = int(sys.stdin.readline()) - floor(int(sys.stdin.readline())/2)


# Print result
print(upper_bulb)
