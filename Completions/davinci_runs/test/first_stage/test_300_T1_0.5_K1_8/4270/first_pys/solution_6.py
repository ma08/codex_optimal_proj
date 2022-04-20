

import sys

def calc_max_value(N, values):
    values.sort()
    while len(values) > 1:
        new = (values[0] + values[1]) / 2
        values = values[2:]
        values.append(new)
        values.sort()
    return values[0]

def main():
    N = int(sys.stdin.readline())
    values = list(map(int, sys.stdin.readline().split()))
    print(calc_max_value(N, values))

if __name__ == '__main__':
    main()