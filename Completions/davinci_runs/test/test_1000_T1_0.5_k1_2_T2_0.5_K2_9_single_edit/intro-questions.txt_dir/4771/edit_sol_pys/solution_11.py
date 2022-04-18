# Problem

# You have a pile of n boxes and a volume v. Each box has a width wi, height hi, and depth di.
# You want to stack the boxes in such a way that the total height of the stack is as large as possible,
# but you cannot stack a box on top of a box with a smaller width, height, or depth.
# What is the height of the highest possible stack?

# Input
# The first line of the input gives the number of test cases, T. T test cases follow.
# Each test case begins with one line containing two integers n and v.
# Then, n lines follow. The i-th line contains three integers wi, hi, and di.

# Output
# For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1)
# and y is the total height of the highest possible stack.

# Limits
# 1 ≤ T ≤ 100.
# 1 ≤ v ≤ 10^9.
# 1 ≤ wi, hi, di ≤ 2*10^9.
# All the w's, h's, and d's will be distinct.
# At least one box will fit into the given volume.

# Small dataset
# 1 ≤ n ≤ 10.

# Large dataset
# 1 ≤ n ≤ 100.

# Sample

# Input
# 3
# 3 10
# 2 2 2
# 2 4 2
# 4 3 3
# 3 8
# 2 2 2
# 2 4 2
# 4 3 3
# 3 8
# 2 2 2
# 2 4 2
# 4 4 4

# Output
# Case #1: 4
# Case #2: 2
# Case #3: 0

# In Sample Case #1, you can stack the boxes in this order:
# 2x2x2
# 2x4x2
# 4x3x3
# The total height is 2+2+3=7.
# In Sample Case #2, the largest possible stack has height 2.
# In Sample Case #3, there is no way to stack the boxes, so the answer is 0.

# Solution

def main():
	# Read the input
	n, v = [int(x) for x in input().split()]
	boxes = []
	for i in range(n):
		boxes.append([int(x) for x in input().split()])
	# Sort the boxes by volume
	boxes.sort(key=lambda box: box[0]*box[1]*box[2], reverse=True)
	# Print the difference between the largest box and the volume required
	print(boxes[0][0]*boxes[0][1]*boxes[0][2]-v)
	
main()
