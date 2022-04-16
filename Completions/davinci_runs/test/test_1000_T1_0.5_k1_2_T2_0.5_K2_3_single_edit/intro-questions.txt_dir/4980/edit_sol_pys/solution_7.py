

import sys

def main():

	n = int(sys.stdin.readline())
	count = 0
	for i in range(n):
		s = sys.stdin.readline().strip()
		if "pink" in s or "rose" in s:
			count += 1

	if count == 0:
		print("I must watch Star Wars with my daughter") # print(0)
	else:
		print(count) # print(count)

main()
