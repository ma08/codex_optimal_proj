

import math

def main():
	x = float(input())
	a, b = math.floor(x), math.ceil(x)
	print(int(a), int(b))

if __name__ == '__main__':
	main()