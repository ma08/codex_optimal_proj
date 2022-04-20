
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
    assert main('000') == 0
    assert main('001') == 0
    assert main('010') == 1
    assert main('011') == 1
    assert main('100') == 0
    assert main('101') == 0
    assert main('110') == 1
    assert main('111') == 2


def main(input):
    s = input
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
    test()
