import sys


def main():
    n = int(sys.stdin.readline())
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    for n in nums:
        print(n)


if __name__ == '__main__':
    main()
