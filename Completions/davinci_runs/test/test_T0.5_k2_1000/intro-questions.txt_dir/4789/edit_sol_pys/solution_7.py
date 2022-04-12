

import sys

def main():
	n = int(sys.stdin.readline())
	desks = [int(sys.stdin.readline()) for _ in range(n)] # list comprehension
	current_desk = 1
	passes = 0
	for desk in desks:
		if desk > current_desk:
			passes = passes + (desk - current_desk)
		current_desk = desk
	print(passes)

if __name__ == '__main__':
	main()
