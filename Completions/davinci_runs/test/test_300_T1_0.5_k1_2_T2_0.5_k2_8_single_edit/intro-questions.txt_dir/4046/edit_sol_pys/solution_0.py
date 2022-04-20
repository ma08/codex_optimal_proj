def main():
    n = int(input())
    q = list(map(int, input().split()))
    print(*solve(n, q))


def solve(n, q):
    p = [1]
    for i in range(n - 1):
        if p[-1] + q[i] > 0 and p[-1] + q[i] <= n:
            p.append(p[-1] + q[i])
        else:
            return -1
    return p


if __name__ == "__main__":
    main()
