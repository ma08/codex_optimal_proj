

import sys

def main():
	k = int(sys.stdin.readline().strip())
	n = int(sys.stdin.readline().strip())
	l = []
	for i in range(n):
		l.append(sys.stdin.readline().strip().split())
		l[i][0] = int(l[i][0]) #convert to int
		l[i][1] = str(l[i][1]) #convert to string
	curr = k
	for i in range(n):
		if l[i][1] == "R":
			curr = (curr+1)%8 #modulo 8
		elif l[i][1] == "L":
			curr = (curr-1)%8 #modulo 8
		if l[i][0] > 210:
			break
	print(curr)

if __name__ == '__main__':
	main()
