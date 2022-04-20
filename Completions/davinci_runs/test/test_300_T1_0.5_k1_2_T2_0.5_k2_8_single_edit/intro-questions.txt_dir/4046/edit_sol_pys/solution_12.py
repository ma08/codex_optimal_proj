
def check(p, q, n):
    for i in range(n - 1):
        if p[i] + q[i] > 0 and p[i] + q[i] <= n:
            p.append(p[i] + q[i])
        else:
            return -1
    return p

def solve(n, q):
    p = [1]
    return check(p, q, n)


def main():
    n = int(input())
    q = list(map(int, input().split()))
    print(*solve(n, q))


if __name__ == "__main__":
    main()
