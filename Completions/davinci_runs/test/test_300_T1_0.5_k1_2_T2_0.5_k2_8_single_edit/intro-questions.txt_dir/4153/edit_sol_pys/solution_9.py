
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


def main2():
	n = int(input())
	a = list(map(int, input().split()))
	ans = 1
	for i in range(n):
		if a[i] == 0:
			ans = 0
			break
		elif a[i] == 2:
			ans *= 2
		elif a[i] == 3:
			ans *= 3
		else:
			ans *= 6
	print(ans)

if __name__ == '__main__':
	main2()
