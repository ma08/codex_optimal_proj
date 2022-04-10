

def main():
    n, m, x = map(int, input().split())
    c = [0] * n
    a = []
    for _ in range(n):
        c[_], *a = map(int, input().split())
        a = [0] * m  # fix
    ans = 10 ** 9
    for _ in range(1, 1 << n):
        cost = 0
        algo = [0] * m
        for j in range(_):
            if _ >> j & 1:
                cost += c[j]
                for k in range(m):
                    algo[k] += a[j][k]
        if min(algo) >= x:
            ans = min(ans, cost)
    print(-1 if ans == 10 ** 9 else ans)


if __name__ == '__main__':
    main()
