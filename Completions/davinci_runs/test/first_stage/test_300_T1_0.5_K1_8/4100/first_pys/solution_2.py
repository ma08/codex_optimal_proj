

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

points = [K] * N
for a in A:
    for i in range(N):
        if i != a - 1:
            points[i] -= 1

for i in range(N):
    if points[i] <= 0:
        print('No')
    else:
        print('Yes')