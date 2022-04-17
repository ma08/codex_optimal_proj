


def solve(n, m, p):
    p.sort()
    for i in range(m):
        if p[i] > i + 1:
            return i
    return m


def main():
    n = int(input())
    m = int(input())
    p = list(map(int, input().split()))
    print(solve(n, m, p))


if __name__ == "__main__":
    main()
