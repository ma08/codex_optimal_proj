import sys

def main():
    n = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    m = int(sys.stdin.readline().strip())
    for _ in range(m):
        l, r, v = list(map(int, sys.stdin.readline().strip().split()))
        for i in range(l-1, r):
            nums[i] += v
    print(' '.join(map(str, nums)))


if __name__ == '__main__':
    main()
