
import math

args = [int(x) for x in input().split()]
n, s = args
holes = []
for i in range(n):
    r, x, y, z = [int(x) for x in input().split()]
    holes.append((r, x, y, z))
holes.sort(key=lambda x: x[3])

# This is the block of cheese that we are currently cutting.
cheese_block = 100000
for i in range(s):
    # Figure out how much cheese we have in this block.
    cheese_weight = 0
    for h in holes:
        if h[3] < cheese_block:
            cheese_weight += (4/3) * math.pi * h[0]**3
        else:
            break

    # Figure out how many slices we can get from this block.
    slices_from_block = cheese_weight / s
    slices_from_block = slices_from_block / (100 * 100 * 100)

    print(slices_from_block * 100)
    cheese_block -= slices_from_block * 100
