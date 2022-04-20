


def main():
    n, x = map(int, input().split())
    xs = list(map(int, input().split()))
    xs.sort()
    ans = float('inf')
    for i in range(n):
        ans = min(ans, max(x - xs[i], xs[i] - x))
    print(ans)


if __name__ == '__main__':
    main()