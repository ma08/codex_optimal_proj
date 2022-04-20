
def solve(n, m):
    if n == 1:
        return 0
    return max(2 * m - n, n - 2 * m)


def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        print(solve(n, m))

if __name__ == '__main__':
    main()
