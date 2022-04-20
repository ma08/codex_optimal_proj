

def main():
    d, g = map(int, input().split())
    p, c = [], []
    for _ in range(d):
        p_i, c_i = map(int, input().split())
        p.append(p_i)
        c.append(c_i)
    ans = float('inf')
    for i in range(2 ** d):
        score = 0
        cnt = 0
        for j in range(d):
            if ((i >> j) & 1):
                score += 100 * (j + 1) * p[j] + c[j]
                cnt += p[j]
        for j in range(d - 1, -1, -1):
            if (score >= g):
                ans = min(ans, cnt)
                break
            if not ((i >> j) & 1):
                for k in range(p[j]):
                    score += 100 * (j + 1)
                    cnt += 1
                    if (score >= g):
                        ans = min(ans, cnt)
                        break
    print(ans)

if __name__ == '__main__':
    main()