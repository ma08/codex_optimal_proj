
import itertools

a, b, c, d = map(int, input().split())

def check(a, b, c, d, op1, op2):
    if op1 == '*':
        if op2 == '*':
            if a * b == c * d:
                return True
        elif op2 == '+':
            if a * b == c + d:
                return True
        elif op2 == '-':
            if a * b == c - d:
                return True
        elif op2 == '/':
            if a * b == c / d and d != 0:
                return True
    elif op1 == '+':
        if op2 == '*':
            if a + b == c * d:
                return True
        elif op2 == '+':
            if a + b == c + d:
                return True
        elif op2 == '-':
            if a + b == c - d:
                return True
        elif op2 == '/':
            if a + b == c / d and d != 0:
                return True
    elif op1 == '-':
        if op2 == '*':
            if a - b == c * d:
                return True
        elif op2 == '+':
            if a - b == c + d:
                return True
        elif op2 == '-':
            if a - b == c - d:
                return True
        elif op2 == '/':
            if a - b == c / d and d != 0:
                return True
    elif op1 == '/':
        if op2 == '*':
            if a / b == c * d:
                return True
        elif op2 == '+':
            if a / b == c + d:
                return True
        elif op2 == '-':
            if a / b == c - d:
                return True
        elif op2 == '/':
            if a / b == c / d and d != 0:
                return True
    return False

def main():
    operators = ['*', '+', '-', '/']
    output = []
    for op1, op2 in itertools.product(operators, repeat=2):
        if check(a, b, c, d, op1, op2):
            output.append(str(a) + ' ' + op1 + ' ' + str(b) + ' = ' + str(c) + ' ' + op2 + ' ' + str(d))
    if len(output) == 0:
        print('No solution')
    else:
        for line in sorted(output):
            print(line)

if __name__ == '__main__':
    main()
