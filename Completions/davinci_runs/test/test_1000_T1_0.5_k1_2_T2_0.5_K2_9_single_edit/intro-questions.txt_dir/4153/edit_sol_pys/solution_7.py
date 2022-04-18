

import sys

def main():
    s = sys.stdin.readline().rstrip()
    stack = []
    ans = 0
    for c in s:
        if c == '0':
            if len(stack) > 0 and stack[-1] == '1':
                stack.pop()
                ans += 1
            else:
                stack.append(c)
        else:
            stack.append(c)
    print(ans)

if __name__ == '__main__':
	n = int(input())
	if n == 0:
		print(0)
		else:
			print(n-1)
