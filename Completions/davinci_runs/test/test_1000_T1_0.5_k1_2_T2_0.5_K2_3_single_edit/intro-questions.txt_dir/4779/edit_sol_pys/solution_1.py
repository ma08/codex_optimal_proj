
import sys


def main():
    n = int(sys.stdin.readline())
    input_list = [int(sys.stdin.readline()) for _ in range(n)]
    input_list.sort()
    max_val = float('-inf')
    for i in range(n):
        if i == 0:
            max_val = max(max_val, input_list[i] * sum(input_list[i + 1:]))
        elif i == n - 1:
            max_val = max(max_val, input_list[i] * sum(input_list[:i]))
        else:
            max_val = max(max_val, input_list[i] * sum(input_list[:i]) + input_list[i] * sum(input_list[i + 1:]))
    print(max_val)


if __name__ == '__main__':
    main()
