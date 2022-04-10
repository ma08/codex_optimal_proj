

def main():
    n, m = map(int, input().split())
    s, d, c = [], [], []
    for i in range(m):
        si, di, ci = map(int, input().split())
        s.append(si)
        d.append(di)
        c.append(ci)
    
    res = [-1] * n
    for i in range(m):
        if s[i] > 1:
            res[s[i] - 2] = 0
        for j in range(c[i]):
            res[s[i] + j - 1] = i + 1
        res[d[i] - 1] = m + 1
    if -1 in res:
        print(-1)
    else:
        print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()