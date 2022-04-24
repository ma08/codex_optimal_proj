
# read N
N = int(input())
# read list
L = [int(i) for i in input().split()]

# create dictionary for numbers
D = {}
for i in range(N):
    D[L[i]] = D.get(L[i], 0) + 1

# create list of numbers
X = []
for i in range(N):
    if D[L[i]] % 2:
        X.append(L[i])

# print numbers
print(X[0], X[1])
