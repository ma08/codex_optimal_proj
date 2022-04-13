import itertools

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
            if a * b == c / d:
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
            if a + b == c / d:
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
            if a - b == c / d:
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
            if a / b == c / d:
                return True
    return False

def main():
    a, b, c, d = map(int, input().split())  # noqa
    operators = ['*', '+', '-', '/']
    output = []
    for op1, op2 in itertools.product(operators, repeat=2):
        if check(a, b, c, d, op1, op2):
            output.append(str(a) + ' ' + op1 + ' ' + str(b) + ' = ' + str(c) + ' ' + op2 + ' ' + str(d))  # noqa
    if len(output) == 0:
        print('problems ahead')
    else:
        for line in sorted(output):
            print(line)

if __name__ == '__main__':
    main()
