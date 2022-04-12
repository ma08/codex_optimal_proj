N = int(input())
T = list(map(int, input().split()))
M = int(input())
P_X = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    P, X = P_X[i]
    print(sum(T) - T[P-1] + X)
