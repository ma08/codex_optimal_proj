

# N = Number of elements
# M = Number of queries
N, M = map(int, input().split())
a = [int(input()) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    l, r, t = b[i]
    for j in range(l-1, r):
        a[j] = t

for i in range(N):
    print(a[i])
