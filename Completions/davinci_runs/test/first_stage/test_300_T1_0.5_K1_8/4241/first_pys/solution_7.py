

import sys

def main():
	s = sys.stdin.readline().strip()
	t = sys.stdin.readline().strip()
	
	count = 0
	
	for i in range(len(t)):
		if s[i] != t[i]:
			count += 1
			
	print(count)
	
if __name__ == '__main__':
	main()