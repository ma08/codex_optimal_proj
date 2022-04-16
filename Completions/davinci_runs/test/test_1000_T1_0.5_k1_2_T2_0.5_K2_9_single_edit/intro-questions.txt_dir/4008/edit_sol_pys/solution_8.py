

def main():
    n, m = map(int, input().split())
    a = [0] * n
    for i in range(n):
        a[i] = list(map(int, input().split()))
    ans = 0
    for i in range(m):
        for j in range(i, m):
            s = 0
            for k in range(n):
                s += max(a[k][i], a[k][j])
            ans = max(ans, s)
    print(ans)


if __name__ == '__main__':
    main()
