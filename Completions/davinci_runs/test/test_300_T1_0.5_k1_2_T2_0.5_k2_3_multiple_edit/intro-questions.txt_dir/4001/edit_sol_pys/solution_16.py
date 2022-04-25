N = int(input())
L = list(map(int, input().split()))
D = {}
for i in L:
    D[i] = D.get(i, 0) + 1
X = []
for i in D:
    if D[i] % 2:
        X.append(i)
print(X[0], X[1])
