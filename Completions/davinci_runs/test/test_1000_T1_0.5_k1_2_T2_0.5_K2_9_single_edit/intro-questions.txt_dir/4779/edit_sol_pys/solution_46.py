
import sys
import bisect


def main():
    n = int(sys.stdin.readline())
    input = [int(sys.stdin.readline()) for _ in range(n)]
    input.sort()
    max_val = float('-inf')
    for i in range(n):
        if i == 0:
            max_val = max(max_val, input[i] * sum(input[i + 1:]))
        elif i == n - 1:
            max_val = max(max_val, input[i] * sum(input[:i]))
        else:
            max_val = max(max_val, input[i] * sum(input[:i]) + input[i] * sum(input[i + 1:]))
    print(max_val)


if __name__ == '__main__':
    main()
