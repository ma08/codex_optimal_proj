


def solve(n, a):
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    d = {}
    for i in range(n + 1):
        if s[i] not in d:
            d[s[i]] = i
        else:
            return i - d[s[i]]
    return 0


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))


if __name__ == '__main__':
    main()
