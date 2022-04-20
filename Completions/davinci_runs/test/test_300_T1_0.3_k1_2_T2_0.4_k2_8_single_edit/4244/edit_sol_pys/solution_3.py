


def solve(n, x):
    x.sort()
    ans = 0
    for i in range(n):
        ans += (x[i] - x[n // 2]) ** 2
    return ans


def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = solve(n, x)

    print(ans)

if __name__ == '__main__':
    main()
