

import sys
import math

def main():
	# Read input
	n, s = map(int, sys.stdin.readline().strip().split())
	holes = []
	for _ in range(n):
		r, x, y, z = map(int, sys.stdin.readline().strip().split())
		holes.append((r, x, y, z))

	# Calculate total volume of the block
	volume = 100 * 100 * 100 * 0.5
	for r, x, y, z in holes:
		volume -= 4/3 * math.pi * r**3

	# Calculate volume of each slice
	volume_per_slice = volume / s

	# Calculate thickness of each slice
	slices = []
	z = 100000
	for _ in range(s):
		volume_in_slice = 0
		for r, x, y, z_hole in holes:
			if z_hole - r < z and z_hole + r > 0:
				volume_in_slice += 4/3 * math.pi * r**3
				if z_hole - r > 0:
					volume_in_slice -= 4/3 * math.pi * (r**3 - (z_hole - z)**3) / 2
				if z_hole + r < 100000:
					volume_in_slice -= 4/3 * math.pi * (r**3 - (z - z_hole)**3) / 2
		z -= volume_per_slice / volume_in_slice * 100000
		slices.append(z)

	# Print result
	for slice in slices:
		print(slice)

if __name__ == "__main__":
	main()
