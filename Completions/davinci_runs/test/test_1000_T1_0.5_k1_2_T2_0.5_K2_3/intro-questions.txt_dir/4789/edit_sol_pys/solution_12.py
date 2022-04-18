

import sys

def main():
	k = int(sys.stdin.readline())
	desks = [int(sys.stdin.readline()) for _ in range(k)]
	current_desk = 1
	passes = 0
	for desk in desks:
		if desk > current_desk:
			passes += (desk - current_desk + 1)
		current_desk = desk
	print(passes)

if __name__ == '__main__':
	main()
