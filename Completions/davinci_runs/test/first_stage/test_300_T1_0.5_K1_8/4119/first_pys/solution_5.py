


def main():
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    ans = x[0] - 1
    for i in range(1, m):
        if x[i] - x[i - 1] > 1:
            ans += x[i] - x[i - 1] - 1
    ans += n - x[-1]
    print(ans)


if __name__ == '__main__':
    main()