
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


def test():
    assert main('101') == 1
    assert main('11001') == 3


def main(s):
	ans = 0
	while True:
		if s.count('01') > 0:
			s = s.replace('01', '', 1)
			ans += 1
		elif s.count('10') > 0:
			s = s.replace('10', '', 1)
			ans += 1
		else:
			break
	print(ans)

if __name__ == '__main__':
	# main()
	test()
