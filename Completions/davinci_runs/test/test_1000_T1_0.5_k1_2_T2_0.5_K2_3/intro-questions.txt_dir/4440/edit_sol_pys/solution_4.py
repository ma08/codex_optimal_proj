
# define the length
import math

# define the max volume
L = int(input())
max_volume = 0
# loop through all the possible values of a and b
for a in range(1, L + 1):
        # calculate the possible value of c
    for b in range(1, L + 1):
        # if c is positive, calculate the volume
        c = L - a - b
        if c > 0:
            volume = a * b * c
            if volume > max_volume:
                max_volume = volume

print(max_volume)
