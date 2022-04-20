
N, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
s = 0
for i in range(K):
    s += R[N - K + i]
print(s / K)
