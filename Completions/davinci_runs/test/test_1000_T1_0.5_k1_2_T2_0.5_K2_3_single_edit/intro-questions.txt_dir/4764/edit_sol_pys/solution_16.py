
import sys
import math

n, h, v = [int(i) for i in sys.stdin.readline().split()]

# Calculate the volume of the cake
volume = n * n * 4

# Calculate the volume of the largest piece of cake
volume_max = max(volume / 4, (n - h) * (n - v) * 4, h * v * 4, h * (n - v) * 4, (n - h) * v * 4)

# Print the volume of the largest piece of cake
print(volume_max)
