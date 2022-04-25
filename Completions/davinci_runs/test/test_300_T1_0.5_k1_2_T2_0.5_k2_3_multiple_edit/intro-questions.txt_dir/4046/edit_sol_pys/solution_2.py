


def solve(n, p):
    p = [1, 1]
    for i in range(n - 1):
        if p[-2] + p[-1] > 0 and p[-2] + p[-1] <= n:
            p.append(p[-2] + p[-1])
        else:
            return -1
    return p


def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(*solve(n, p))


if __name__ == "__main__":
    main()
