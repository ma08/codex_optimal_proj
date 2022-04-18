

import sys

def get_input():
	n = int(sys.stdin.readline().strip())
	l = []
	for i in range(n):
		l.append(sys.stdin.readline().strip().split())
		l[i][0] = int(l[i][0])
		l[i][1] = str(l[i][1])
	return n, l

def get_output(l):
	for i in range(n):
		if l[i][0] > 210:
			break
		if l[i][1] == "T":
			curr = (curr+1)%8
		elif l[i][1] == "N":
			curr = (curr-1)%8
	return curr
import sys

def main():
	k = int(sys.stdin.readline().strip())
	n, l = get_input()
	curr = k
	print(get_output(l))

if __name__ == '__main__':
	main()
