

import sys

def main():
	k = int(sys.stdin.readline().strip())
	n = int(sys.stdin.readline().strip())
	l = []
	for i in range(n):
		l.append(sys.stdin.readline().strip().split())
		l[i][0] = int(l[i][0]) #time
		l[i][1] = str(l[i][1]) #direction
	curr = k
	for i in range(n):
		if l[i][1] == "T":
			curr = (curr+1)%8 #clockwise
		elif l[i][1] == "F":
			curr = (curr-1)%8 #counterclockwise
		if l[i][0] > 210:
			break
	print(curr)

if __name__ == '__main__':
	main()
