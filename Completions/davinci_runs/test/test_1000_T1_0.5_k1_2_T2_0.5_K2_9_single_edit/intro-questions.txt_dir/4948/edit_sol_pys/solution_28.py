

import sys
import math

def main():
	# Read input
	n, s = map(int, sys.stdin.readline().strip().split())
	holes = []
	for _ in range(n):
		r, x, y, z = map(int, sys.stdin.readline().strip().split())
		holes.append((r, x, y, z))

	# Calculate total weight of the block
	weight = 100 * 100 * 100 * 0.5 # half of the block
	for r, x, y, z in holes:
		weight -= 4/3 * math.pi * r**3

	# Calculate weight of each slice
	weight_per_slice = weight / s # weight of each slice

	# Calculate thickness of each slice
	slices = []
	z = 100000 # thickness of the block
	for _ in range(s):
		weight_in_slice = 0 # weight of slice
		for r, x, y, z_hole in holes:
			if z_hole - r < z and z_hole + r > 0: # if the hole is within the slice
				weight_in_slice += 4/3 * math.pi * r**3
				if z_hole - r > 0: # if the hole is not at the bottom of the block
					weight_in_slice -= 4/3 * math.pi * (r**3 - (z_hole - z)**3) # subtract weight of the part not in the slice
				if z_hole + r < 100000: # if the hole is not at the top of the block
					weight_in_slice -= 4/3 * math.pi * (r**3 - (z - z_hole)**3) # subtract weight of the part not in the slice
		z -= weight_per_slice / weight_in_slice * 100000
		slices.append(z)

	# Print result
	for slice in slices:
		print(slice)

if __name__ == "__main__":
	main()
