


def solve(n, a):
    mx = max(a)
    mn = min(a)
    if mx == mn:
        return 'YES'
    if mx - mn > 1:
        return 'NO'
    if a.count(mx) > 1 and a.count(mn) > 1:
        return 'NO'
    return 'YES'


def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))


if __name__ == "__main__":
    main()
