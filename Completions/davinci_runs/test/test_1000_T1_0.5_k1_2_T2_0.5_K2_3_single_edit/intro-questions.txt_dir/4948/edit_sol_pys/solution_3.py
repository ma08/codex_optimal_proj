

import sys
import math

def find_weight(r, x, y, z, t):
    if z + r < t:
        return 0
    elif z - r > t * 100:
        return 4.0/3.0 * math.pi * r**3
    else:
        return (4.0/3.0 * math.pi * r**3) - (1.0/3.0 * math.pi * (r - ((t * 100) - z))**3)

def find_slices(n, s, holes):
    total_weight = 0
    for r, x, y, z in holes:
        total_weight += 4.0/3.0 * math.pi * r**3
    slice_weight = total_weight / s
    slices = []
    for i in range(s):
        slices.append(0)
    for r, x, y, z in holes:
        for i in range(s):
            slices[i] += find_weight(r, x, y, z, i)
    weight = 0
    for i in range(s):
        weight += slices[i]
        slices[i] = slice_weight - slices[i]
    slices[-1] += weight - (slice_weight * s)
    return slices

def main():
    n, s = [int(x) for x in sys.stdin.readline().split()]
    holes = []
    for i in range(n):
        r, x, y, z = [int(x) for x in sys.stdin.readline().split()]
        holes.append((r, x, y, z))
    slices = find_slices(n, s, holes)
    for t in slices:
        print("{:.10f}".format(t/1000.0))

if __name__ == '__main__':
    main()
