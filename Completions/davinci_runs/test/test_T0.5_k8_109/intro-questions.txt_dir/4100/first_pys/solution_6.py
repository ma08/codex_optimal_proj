

N, K, Q = map(int, input().split())
A = [int(input()) for _ in range(Q)]

scores = [K for _ in range(N)]
for a in A:
    scores[a-1] += 1

for s in scores:
    if s > 0:
        print("Yes")
    else:
        print("No")