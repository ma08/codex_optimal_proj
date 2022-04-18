

from sys import stdin

def main():
	n = int(stdin.readline())
	c = [int(x) for x in stdin.readline().split()]
	c.sort()
	if c[0] > 0:
		print('impossible')
	else:
		ans = 1
		for i in range(1,n):
			ans = min(ans,c[i]//i)
		print(ans)

main()
