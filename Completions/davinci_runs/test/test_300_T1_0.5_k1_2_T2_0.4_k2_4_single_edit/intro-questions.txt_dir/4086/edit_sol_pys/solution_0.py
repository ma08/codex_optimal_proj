

from collections import deque


def main():
    nums = deque(map(int, input().split()))
    print(len(set(nums)))
    print(*sorted(set(nums)))


if __name__ == '__main__':
    main()
