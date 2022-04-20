
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
    assert main('00011') == 1
    assert main('11111') == 0
    assert main('111000111') == 3


def main(s):
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
    return ans


if __name__ == '__main__':
    main()
