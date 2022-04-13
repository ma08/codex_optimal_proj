

import sys

def main():
	k = int(sys.stdin.readline().strip())
	n = int(sys.stdin.readline().strip())
	l = []
	for i in range(n):
		temp = sys.stdin.readline().strip().split()
		temp[0] = int(temp[0])
		temp[1] = str(temp[1])
		l.append(temp)
	curr = k
	for i in range(n):
		if l[i][1] == "T":
			curr = (curr+1)%8
		elif l[i][1] == "F":
			curr = (curr-1)%8
		if l[i][0] > 210:
			break
	print(curr)

if __name__ == '__main__':
	main()
