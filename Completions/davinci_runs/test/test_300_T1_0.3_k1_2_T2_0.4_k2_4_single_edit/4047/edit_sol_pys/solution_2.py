import sys
sys.setrecursionlimit(10**6)


def main():
    n = int(input())
    x = list(map(int, input().split()))

    x.sort()

    ans = 0
    for i in range(1, n):
        if x[i] - x[i-1] > 1:
            ans += x[i] - x[i-1] - 1

    print(ans)

if __name__ == '__main__':
    main()
