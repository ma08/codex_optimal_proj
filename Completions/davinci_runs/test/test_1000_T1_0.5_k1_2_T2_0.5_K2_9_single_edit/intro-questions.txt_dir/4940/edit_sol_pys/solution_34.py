

def main():
    n, m = map(int, input().split())
    p = [list(map(int, input().split())) for _ in range(m)]
    t = [0] * m
    for j in range(m):
        for i in range(m):
            if t[i] < max(t):
                t[i] = max(t)
            t[i] += p[j][i]
    print(*t)

if __name__ == '__main__':
    main()
