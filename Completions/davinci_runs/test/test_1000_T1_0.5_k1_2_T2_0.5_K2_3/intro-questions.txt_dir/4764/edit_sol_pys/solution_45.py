

import sys
import math

n, h, v = [int(i) for i in sys.stdin.readline().split()]

# Calculate the volume of the cake and the volume of the largest piece of the cake
volume = n ** 2 * 4
volume_max = max(volume / 4, (n - h) * (n - v) * 4, h * v * 4, h * (n - v) * 4, (n - h) * v * 4)

# Print the volume of the largest piece of the cake in cubic meters
print(volume_max)
