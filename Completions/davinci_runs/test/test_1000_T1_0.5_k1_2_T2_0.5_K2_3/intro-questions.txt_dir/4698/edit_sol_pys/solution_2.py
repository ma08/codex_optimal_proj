N = int(input())
T = list(map(int, input().split()))
M = int(input())
PX = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    P, X = PX[i]
    print(sum(T) - T[P-1] + X)
