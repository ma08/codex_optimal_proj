


def solve(n, p):
    p = [1, 2]
    for i in range(n - 1):
        if p[-1] + p[i] > 0 and p[-1] + p[i] <= n and p[-1] + p[i] not in p:
            p.append(p[-1] + p[i])
        else:
            return -1
    return p


def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(*solve(n, p))


if __name__ == "__main__":
    main()
