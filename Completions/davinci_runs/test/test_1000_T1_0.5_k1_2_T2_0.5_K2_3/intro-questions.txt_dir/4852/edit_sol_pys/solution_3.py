
import sys

def parse(s, i, op, op_prev, num_prev):
    num = int(s[i])
    if i == len(s) - 1:
        if op_prev == '+':
            return num_prev + num
        elif op_prev == '*':
            return num_prev * num
        else:
            return num
    if s[i + 1] == '+':
        if op_prev == '+':
            return parse(s, i + 2, '+', op, num_prev + num) + parse(s, i + 2, '*', op, num_prev + num)
        elif op_prev == '*':
            return parse(s, i + 2, '+', op, num_prev * num) + parse(s, i + 2, '*', op, num_prev * num)
        else:
            return parse(s, i + 2, '+', op, num) + parse(s, i + 2, '*', op, num)
    elif s[i + 1] == '*':
        if op_prev == '+':
            return parse(s, i + 2, '+', op, num_prev + num) + parse(s, i + 2, '*', op, num_prev + num)
        elif op_prev == '*':
            return parse(s, i + 2, '+', op, num_prev * num) + parse(s, i + 2, '*', op, num_prev * num)
        else:
            return parse(s, i + 2, '+', op, num) + parse(s, i + 2, '*', op, num)

s = sys.stdin.readline()
s = s[:-1]
print parse(s, 0, '+', '+', 0)
