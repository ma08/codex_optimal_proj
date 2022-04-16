

import sys

def main():
	k = int(sys.stdin.readline().strip())
	n = int(sys.stdin.readline().strip())
	l = []
	for i in range(n):
		l.append(sys.stdin.readline().strip().split())
		l[i][0] = int(l[i][0])
		l[i][1] = l[i][1]
	curr = k
	for i in range(n):
		if l[i][1] == 'T':
			curr = (curr+1)%8
		elif l[i][1] == 'N':
			curr = (curr-1)%8
		if l[i][0] > 210:
			break
	print(curr)

if __name__ == '__main__':
	main()
