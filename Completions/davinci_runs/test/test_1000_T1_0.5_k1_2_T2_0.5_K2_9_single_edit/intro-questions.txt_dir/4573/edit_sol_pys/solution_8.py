
N = int(input())
X = list(map(int, input().split()))
X.sort()

for i in range(N):
    print(X[N//2])
