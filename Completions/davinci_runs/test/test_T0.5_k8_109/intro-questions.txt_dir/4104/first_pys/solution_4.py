

import sys

def main():
    expr = sys.stdin.readline().strip()
    expr_list = expr.split('+')
    result = 0
    for num in expr_list:
        num_list = num.split('-')
        for n in num_list:
            result += int(n)
    print(result)

if __name__ == '__main__':
    main()