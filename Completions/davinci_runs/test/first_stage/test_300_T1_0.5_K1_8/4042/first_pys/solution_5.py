

import sys

def main():
	x = float(sys.stdin.readline())
	a = int(x)
	b = int((x-a)*100)
	print(a+1, b+1)
	
if __name__ == '__main__':
	main()