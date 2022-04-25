


def solve(n, p):
    p = [p[0]]
    for i in range(n - 1):
        if p[-1] + p[i] > 0 and p[-1] + p[i] < n:
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
