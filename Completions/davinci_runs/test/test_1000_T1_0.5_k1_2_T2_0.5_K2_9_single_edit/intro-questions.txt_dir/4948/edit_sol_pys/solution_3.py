

import sys
import math

def main():
    n, s = map(int, sys.stdin.readline().split())
    holes = []
    for i in range(n):
        r, x, y, z = map(int, sys.stdin.readline().split())
        holes.append((r, x, y, z))
    print(solve(holes, s))

def solve(holes, s):
    # Get the cheese's volume by subtracting the holes' volumes from the total cheese volume.
    total_cheese_volume = 1000000
    for hole in holes:
        total_cheese_volume -= 4/3 * math.pi * hole[0]**3
    slice_volume = total_cheese_volume / s

    # Find the z-values of the slices (the z-value of the top slice's bottom edge is 0).
    z_values = []
    z = 0.0
    while z < 100000:
        # Subtract the volume of the cheese above this z-value.
        z_values.append(z)
        for hole in holes:
            if z < hole[3] - hole[0]:
                continue
            # Find the z-value of the top of the hole.
            z_top = hole[3] + hole[0] + 0.000001
            if z_top <= z:
                continue
            # Find the z-value of the bottom of the hole.
            z_bottom = hole[3] - hole[0] - 0.000001
            if z_bottom >= z:
                z_bottom = z
            # Find the volume of the hole between z and z_top.
            hole_volume = 4/3 * math.pi * hole[0]**3
            hole_volume -= 4/3 * math.pi * abs(hole[0]**3 - (z_top - hole[3])**3) - 0.000001
            hole_volume -= 4/3 * math.pi * abs(hole[0]**3 - (hole[3] - z_bottom)**3) - 0.000001
            slice_volume -= hole_volume
        z += slice_volume**(1/3)

    return "".join(["{:.9f}\n".format(z_values[i+1] - z_values[i]) for i in range(s)])

if __name__ == "__main__":
    main()
