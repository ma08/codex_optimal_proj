
import sys

rows, cols = map(int, sys.stdin.readline().split()) 

# Just count the number of free spaces 
free = 0 
for i in range(rows):
	for j in range(cols):
		if sys.stdin.read(1) == '.':
			free += 1
		sys.stdin.read(1)

# Squash 0, 1, 2, 3, or 4 cars 
print(free) 
print(free - 2*cols) 
print(free - 4*cols) 
print(free - 6*cols) 
print(free - 8*cols) 
