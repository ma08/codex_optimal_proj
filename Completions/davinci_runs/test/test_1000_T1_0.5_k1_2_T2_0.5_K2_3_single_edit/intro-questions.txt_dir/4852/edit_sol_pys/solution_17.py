
import sys

def parse(s, i, op_prev, op, prev):
    if i == len(s) - 1: return 1
    if s[i + 1] == '+':
        if op_prev == '+':
            return parse(s, i + 2, op_prev, '+', int(s[i])) + parse(s, i + 2, op_prev, '*', int(s[i]))
        elif op_prev == '*':
            return parse(s, i + 2, op_prev, '+', prev * int(s[i])) + parse(s, i + 2, op_prev, '*', prev * int(s[i]))
    elif s[i + 1] == '*':
        if op_prev == '+':
            return parse(s, i + 2, op_prev, '+', int(s[i])) + parse(s, i + 2, op_prev, '*', int(s[i]))
        elif op_prev == '*':
            return parse(s, i + 2, op_prev, '+', prev * int(s[i])) + parse(s, i + 2, op_prev, '*', prev * int(s[i]))

# get the input
s = sys.stdin.readline()
# remove the newline character from the string
s = s[:-1]
# call the function to get the number of distinct values
print parse(s, 0, '+', '+')
