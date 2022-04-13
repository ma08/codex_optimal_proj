
import sys


def main():
    # number of elements
    n = int(sys.stdin.readline())
    # sorted array
    a = sorted(map(int, sys.stdin.readline().split()))
    # initialize ans
    ans = 0
    # for loop
    for i in range(n):
        if a[i] < i + 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
