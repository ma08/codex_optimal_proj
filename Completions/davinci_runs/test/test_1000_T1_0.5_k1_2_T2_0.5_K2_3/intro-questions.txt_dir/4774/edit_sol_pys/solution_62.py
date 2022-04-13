
from itertools import permutations

def is_valid(a, b, c, d, op1, op2):
    if op1 == '*' and op2 == '+':
        return a * b == c + d
    if op1 == '*' and op2 == '-':
        return a * b == c - d
    if op1 == '*' and op2 == '/':
        return a * b == c // d
    if op1 == '+' and op2 == '*':
        return a + b == c * d
    if op1 == '+' and op2 == '-':
        return a + b == c - d
    if op1 == '+' and op2 == '/':
        return a + b == c // d
    if op1 == '-' and op2 == '*':
        return a - b == c * d
    if op1 == '-' and op2 == '+':
        return a - b == c + d
    if op1 == '-' and op2 == '/':
        return a - b == c // d
    if op1 == '/' and op2 == '*':
        return a // b == c * d
    if op1 == '/' and op2 == '+':
        return a // b == c + d
    if op1 == '/' and op2 == '-':
        return a // b == c - d

def main():
    a, b, c, d = map(int, input().split())
    ops = ['+', '-', '*', '/']
    valid = []
    for op1, op2 in permutations(ops, 2):
        if is_valid(a, b, c, d, op1, op2):
            valid.append(str(a) + ' ' + op1 + ' ' + str(b) + ' = ' + str(c) + ' ' + op2 + ' ' + str(d))
    if not valid:
        print('no solution')
    else:
        for e in sorted(valid):
            print(e)

if __name__ == "__main__":
    main()
