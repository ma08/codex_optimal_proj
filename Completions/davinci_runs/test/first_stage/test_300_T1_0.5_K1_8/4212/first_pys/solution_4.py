

def main():
    """main function"""
    # read input
    n, m, q = map(int, input().split())
    a, b, c, d = [], [], [], []
    for _ in range(q):
        tmpa, tmpb, tmpc, tmpd = map(int, input().split())
        a.append(tmpa)
        b.append(tmpb)
        c.append(tmpc)
        d.append(tmpd)

    # calculate
    ans = 0
    for _ in range(2**n):
        seq = [0] * n
        for j in range(n):
            seq[j] = int(bin(i >> j)[2:])
        score = 0
        for j in range(q):
            if seq[b[j] - 1] - seq[a[j] - 1] == c[j]:
                score += d[j]
        ans = max(ans, score)

    print(ans)

if __name__ == '__main__':
    main()