

import sys

def main():
	meal = []
	for line in sys.stdin:
		meal.append([int(x) for x in line.split()])
	meal.pop(0)

	print(meal)

if __name__ == '__main__':
	main()
