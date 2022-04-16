

import sys
import math

def main():
	# Read input
	n, s = map(int, sys.stdin.readline().strip().split())
	holes = set()
	for _ in range(n):
		r, x, y, z = map(int, sys.stdin.readline().strip().split())
		for x_ in range(x - r, x + r):
			for y_ in range(y - r, y + r):
				for z_ in range(z - r, z + r):
					if (x_ - x)**2 + (y_ - y)**2 + (z_ - z)**2 <= r**2:
						holes.add((x_, y_, z_))

	# Calculate total volume of the block
	volume = 100 * 100 * 100
	for x, y, z in holes:
		volume -= 1

	# Calculate volume of each slice
	volume_per_slice = volume / s

	# Calculate thickness of each slice
	slices = []
	z = 100000
	for _ in range(s):
		volume_in_slice = 0
		for x, y, z_hole in holes:
			if z_hole < z:
				volume_in_slice += 1
		z -= volume_per_slice / volume_in_slice * 100000
		slices.append(z)

	# Print result
	for slice in slices:
		print(slice)

if __name__ == "__main__":
	main()
