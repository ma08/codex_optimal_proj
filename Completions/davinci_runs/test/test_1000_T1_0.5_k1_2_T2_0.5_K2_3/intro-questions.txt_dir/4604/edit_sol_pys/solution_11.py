

N, M = map(int, input().split())

a = [0] * N

for _ in range(M):
    s, t = map(int, input().split())
    a[s-1] += 1
    a[t-1] += 1

print("\n".join(map(str, a)))
