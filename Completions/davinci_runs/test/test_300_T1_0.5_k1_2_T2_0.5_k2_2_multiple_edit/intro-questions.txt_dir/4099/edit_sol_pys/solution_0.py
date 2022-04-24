N, K, M = map(int, input().split()) # N問出題される問題数、K個以上満点を取ると合格、M点が平均点
A = list(map(int, input().split())) # N個の得点

sumA = sum(A)
avg = sumA / N

if avg >= M:
    print(0)
    exit()

if K <= M:
    print(-1)
    exit()

print(M*N - sumA)
