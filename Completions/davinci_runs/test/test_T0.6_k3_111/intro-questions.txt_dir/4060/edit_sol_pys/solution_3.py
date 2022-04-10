
import sys


def main():
    n = int(sys.stdin.readline())
    brackets = list(sys.stdin.readline().strip())

    count = 0 

    for i in range(n):
        if brackets[i] == ')':
            brackets[i] = '('
            if check(brackets):
                count += 1
            brackets[i] = ')'
        else:
            brackets[i] = ')'
            if check(brackets):
                count += 1
            brackets[i] = '('
    print(count)


def check(brackets):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return not stack


if __name__ == '__main__':
    main()
