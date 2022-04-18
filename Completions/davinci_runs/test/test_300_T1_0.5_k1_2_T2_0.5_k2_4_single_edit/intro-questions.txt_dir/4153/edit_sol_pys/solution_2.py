

import sys

def main():
	s = sys.stdin.readline().rstrip()
	stack = [0]
	ans = 0
	for c in s:
		if c == ')':
			if stack[-1] == '(':
				stack.pop()
			else:
				stack.append(0)
		else:
			stack.append(c)
	print(ans)

if __name__ == '__main__':
	main()
