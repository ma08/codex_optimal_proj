

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

points = [K]*N

for a in A:
    points[a-1] += 1
    for i in range(N):
        if i == a-1:
            continue
        points[i] -= 1

for p in points:
    if p > 0:
        print("Yes")
    else:
        print("No")