

def main():
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    ans = 10 ** 9
    for i in range(n - m + 1):
        ans = min(ans, l[i + m - 1] - l[i])
    print(ans)


if __name__ == '__main__':
    main()
