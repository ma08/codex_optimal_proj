

import sys
import bisect


def main():
    n = int(sys.stdin.readline())
    inputs = [int(sys.stdin.readline()) for _ in range(n)]
    inputs.sort()
    max_val = float('-inf')
    for i in range(n):
        if i == 0:
            max_val = max(max_val, inputs[i] * sum(inputs[i + 1:]))
        elif i == n - 1:
            max_val = max(max_val, inputs[i] * sum(inputs[:i]))
        else:
            max_val = max(max_val, inputs[i] * sum(inputs[:i]) + inputs[i] * sum(inputs[i + 1:]))
    print(max_val)


if __name__ == '__main__':
    main()
