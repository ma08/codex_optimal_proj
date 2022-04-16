
import math

L = int(input())
max_volume = 0

for a in range(1, L + 1):
    for b in range(1, L + 1):
        c = L - a - b
        if c > 0:
            volume = a * b * c
            if volume > max_volume:
                max_volume = volume

print(max_volume)
