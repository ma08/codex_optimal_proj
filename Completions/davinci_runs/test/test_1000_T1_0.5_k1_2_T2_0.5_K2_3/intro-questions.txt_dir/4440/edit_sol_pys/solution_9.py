# import math
import math

# define the length
L = int(input("Enter the length of the rod: "))
max_volume = 0  # define the max volume
# loop through all the possible values of a, b and c

for a in range(1, L + 1):
    for b in range(1, L + 1):
        c = L - a - b
        if c > 0:  # if c is positive, calculate the volume
            volume = a * b * c
            if volume > max_volume:
                max_volume = volume

print(max_volume)
