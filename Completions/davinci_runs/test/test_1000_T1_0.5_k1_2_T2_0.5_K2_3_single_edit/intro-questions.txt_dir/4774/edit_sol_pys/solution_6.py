
import itertools

a, b, c, d = map(int, input().split())

def check(a, b, c, d, op1, op2):
    for op1, op2 in itertools.product(operators, repeat=2):
        if eval(str(a) + op1 + str(b)) == eval(str(c) + op2 + str(d)):
            return True
    return Falsea

def main():
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
