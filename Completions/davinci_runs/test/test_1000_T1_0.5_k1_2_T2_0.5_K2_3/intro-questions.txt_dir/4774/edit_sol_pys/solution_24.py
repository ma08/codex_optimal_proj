import itertools

def check(a, b, c, d, op1, op2):
    if op1 == '*' and op2 == '*':
        return a * b == c * d
    elif op1 == '*' and op2 == '+':
        return a * b == c + d
    elif op1 == '*' and op2 == '-':
        return a * b == c - d
    elif op1 == '*' and op2 == '/':
        return a * b == c / d
    elif op1 == '+' and op2 == '*':
        return a + b == c * d
    elif op1 == '+' and op2 == '+':
        return a + b == c + d
    elif op1 == '+' and op2 == '-':
        return a + b == c - d
    elif op1 == '+' and op2 == '/':
        return a + b == c / d
    elif op1 == '-' and op2 == '*':
        return a - b == c * d
    elif op1 == '-' and op2 == '+':
        return a - b == c + d
    elif op1 == '-' and op2 == '-':
        return a - b == c - d
    elif op1 == '-' and op2 == '/':
        return a - b == c / d
    elif op1 == '/' and op2 == '*':
        return a / b == c * d
    elif op1 == '/' and op2 == '+':
        return a / b == c + d
    elif op1 == '/' and op2 == '-':
        return a / b == c - d
    elif op1 == '/' and op2 == '/':
        return a / b == c / d

def main():
    a, b, c, d = map(int, input().split())
    operators = ['*', '+', '-', '/']
    output = []
    for op1, op2 in itertools.product(operators, repeat=2):
        if check(a, b, c, d, op1, op2):
            output.append(str(a) + ' ' + op1 + ' ' + str(b) + ' = ' + str(c) + ' ' + op2 + ' ' + str(d))
    if len(output) == 0:
        print('problems ahead')
    else:
        for line in sorted(output):
            print(line)

if __name__ == '__main__':
    main()
