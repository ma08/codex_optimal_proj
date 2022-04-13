

N, M, R = map(int, input().split())
r = list(map(int, input().split()))
G = [[] for i in range(N)]
for i in range(R):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

r.sort()
ans = 10**9
for i in range(M):
    for j in range(i+1, M):
        for k in range(j+1, M):
            d = [False]*N
            d[r[i]] = d[r[j]] = d[r[k]] = True
            q = [(r[i], 0), (r[j], 0), (r[k], 0)]
            while q:
                v, c = q.pop()
                for e in G[v]:
                    if not d[e]:
                        d[e] = True
                        q.append((e, c+1))
            if all(d):
                ans = min(ans, c)

if ans == 10**9:
    print(-1)
else:
    print(ans)
