
import sys
import math

def main():
    args = sys.stdin.readlines()
    n, s = [int(x) for x in args[0].split()]
    holes = [tuple([int(x) for x in args[i].split()]) for i in range(1, n+1)]
    holes.sort(key=lambda x: x[2])

    # This is the block of cheese that we are currently cutting.
    cheese_block = 100000.0
    for i in range(s):
        # Figure out how much cheese we have in this block.
        cheese_weight = 0
        for h in holes:
            if h[2] < cheese_block:
                cheese_weight += (4/3) * math.pi * h[0]**3
            else:
                break

        # Figure out how many slices we can get from this block.
        slices_from_block = cheese_weight / (s * (100 * 100 * 100))

        print(slices_from_block * 100)
        cheese_block -= slices_from_block * 100

if __name__ == '__main__':
    main()
