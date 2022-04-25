

A = [list(map(int, input().split())) for _ in range(K)]
N, K = map(int, input().split())

ans = N - len(set([a for _ in A for a in _]))
print(ans)
