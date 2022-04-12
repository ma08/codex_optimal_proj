
import sys


def main():
    n = int(sys.stdin.readline())
    arr = [int(sys.stdin.readline()) for _ in range(n)]
    arr.sort()
    max_val = float('-inf')
    for i in range(n):
        if i == 0:
            max_val = max(max_val, arr[i] * sum(arr[i + 1:]))
        elif i == n - 1:
            max_val = max(max_val, arr[i] * sum(arr[:i]))
        else:
            max_val = max(max_val, arr[i] * sum(arr[:i]) + arr[i] * sum(arr[i + 1:]))
    print(max_val)


if __name__ == '__main__':
    main()
