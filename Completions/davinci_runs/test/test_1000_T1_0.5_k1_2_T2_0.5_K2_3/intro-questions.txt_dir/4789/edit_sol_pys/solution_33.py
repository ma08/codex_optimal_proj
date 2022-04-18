

import sys

def main():
	k = int(sys.stdin.readline())
	doors = [int(sys.stdin.readline()) for _ in range(k)]
	current_door = 1
	steps = 0
	for door in doors:
		if door > current_door:
			steps += (door - current_door)
		current_door = door
	print(steps)

if __name__ == '__main__':
	main()
