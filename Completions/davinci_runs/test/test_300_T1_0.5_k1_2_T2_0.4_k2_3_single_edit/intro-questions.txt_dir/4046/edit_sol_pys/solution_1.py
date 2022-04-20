


def check(p, q):
    for i in range(len(q)):
        if p[i] + q[i] > 0 and p[i] + q[i] <= len(q):
            p.append(p[-1] + q[i])
        else:
            return False
    return True


def solve(n, q):
    p = [1]
    for i in range(n - 1):
        if not check(p, q):
            return -1
    return p


def main():
    n = int(input())
    q = list(map(int, input().split()))
    print(*solve(n, q))


if __name__ == "__main__":
    main()
