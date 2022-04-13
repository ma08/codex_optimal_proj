

import sys
import math

def find_weight(r, x, y, z, t, s):
    if z + r < t:
        return 0, 0
    elif z - r > t:
        return 4.0/3.0 * math.pi * r**3, 4.0/3.0 * math.pi * r**3
    else:
        return ((4.0/3.0 * math.pi * r**3) - (1.0/3.0 * math.pi * (r - (t - z))**3), 4.0/3.0 * math.pi * r**3)

def find_slices(n, s, holes):
    total_weight = 0.0
    total_volume = 0.0
    for r, x, y, z in holes:
        total_weight += 4.0/3.0 * math.pi * r**3
        total_volume += 4.0/3.0 * math.pi * r**3
    slice_volume = total_volume / s
    slices = []
    for i in range(s):
        slices.append(0)
    for r, x, y, z in holes:
        for i in range(s):
            slices[i] += find_weight(r, x, y, z, i * 100, s)[0]
    weight = 0.0
    for i in range(s):
        weight += slices[i]
        slices[i] = slice_volume - slices[i]
    slices[-1] += weight - (slice_volume * s)
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
