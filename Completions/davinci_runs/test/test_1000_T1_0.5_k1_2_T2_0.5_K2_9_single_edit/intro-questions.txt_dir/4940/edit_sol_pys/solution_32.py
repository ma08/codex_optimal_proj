

def main():
    n, m = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(m)]
    t = [0] * n
    for j in range(m):
        for i in range(n):
            if t[i] < max(t[:i]):
                t[i] = max(t[:i])
            t[i] += p[j][i]
    print(*t)

if __name__ == '__main__':
    main()
