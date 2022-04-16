

import sys
sys.stdin = open('input.txt')

M, N = map(int, input().split())
T = list(map(int, input().split()))
X = list(map(int, input().split()))

D = []
T = []
S = []
D2 = []

for i in range(M-1):
    for j in range(N-1):
        D = [X[j+1]-X[j] for j in range(N-1)]
        T = [T[i+1]-T[i] for i in range(M-1)]
        S = [D[i]/T[i] for i in range(M-1)]
        D2 = [S[i]*T[0] for i in range(M-1)]

D2 = sorted(D2)

D2 = list(set(D2))

print(len(D2))
print(*D2)
