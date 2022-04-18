

import sys
import math

def main():
    args = sys.stdin.readlines()
    n, s = [int(x) for x in args[0].split()]
    holes = []
    for i in range(1, n+1):
        r, x, y, z = [int(x) for x in args[i].split()]
        holes.append((r, x, y, z))
    holes.sort(key=lambda x: x[3], reverse=True)

    # This is the block of cheese that we are currently cutting
    cheese_block = 100000
    for i in range(s-1):
        # Figure out how much cheese we have in this block
        cheese_weight = 0
        for h in holes:
            if h[3] < cheese_block:
                cheese_weight += (4/3) * math.pi * h[0]**3
            else:
                break

        # Figure out how many slices we can get from this block
        slices_from_block = cheese_weight / s
        slices_from_block = slices_from_block / (100 * 100 * 100)

        print(slices_from_block * 100)
        cheese_block -= slices_from_block * 100

if __name__ == '__main__':
    main()
