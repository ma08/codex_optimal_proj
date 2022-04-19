
# ===

D, G = map(int, input().split())
p, c = [], []
for i in range(D):
    pi, ci = map(int, input().split())
    p.append(pi)
    c.append(ci)

# ===

ans = float('inf')
for i in range(2**D):
    s = 0
    cnt = 0
    for j in range(D):
        if (i >> j) & 1:
            s += 100*(j+1)*p[j] + c[j]
            cnt += p[j]
    for j in range(D-1, -1, -1):
        if (i >> j) & 1:
            continue
        for k in range(p[j]):
            if s >= G:
                break
            s += 100*(j+1)
            cnt += 1
        if s >= G:
            break
    ans = min(ans, cnt)

print(ans)
