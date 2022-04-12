
from itertools import permutations

def is_valid(a, b, c, d, op1, op2):
    return eval(f'{a}{op1}{b}') == eval(f'{c}{op2}{d}')

def main():
    a, b, c, d = map(int, input().split())
    ops = ['+', '-', '*', '/']
    valid = []
    for op1, op2 in permutations(ops, 2):
        if is_valid(a, b, c, d, op1, op2):
            valid.append(f'{a} {op1} {b} = {c} {op2} {d}')
    if not valid:
        print('problem ahead')
    else:
        for e in sorted(valid):
            print(e)

if __name__ == "__main__":
    main()
