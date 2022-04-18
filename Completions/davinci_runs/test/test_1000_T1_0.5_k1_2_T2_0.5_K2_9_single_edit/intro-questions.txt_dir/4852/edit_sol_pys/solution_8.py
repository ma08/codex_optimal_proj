
import sys


def parse(s, i, op, op_prev):
    num = int(s[i])
    if i == len(s) - 1:
        return 1
    if s[i + 1] == '+':
        return parse(s, i + 2, '+', op) + parse(s, i + 2, '*', op)
    elif s[i + 1] == '*':
        if op_prev == '+':
            return parse(s, i + 2, '+', op) + parse(s, i + 2, '*', op)
        elif op_prev == '*':
            return parse(s, i + 2, '+', op) * parse(s, i + 2, '*', op)

s = sys.stdin.readline()
s = s[:-1]
print parse(s, 0, '+', '+')
