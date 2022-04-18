from collections import deque


def main():
    n = int(input())
    stack = deque(input().split())
    max_length = 0
    current_length = 0
    for i in range(n):
        if stack[i] == '1':
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 0
    max_length = max(max_length, current_length)
    print(max_length)


if __name__ == '__main__':
    main()
