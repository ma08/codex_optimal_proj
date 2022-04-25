
# read N
N = int(input())
# read list
L = list(map(int, input().split()))

# create dictionary for elements
D = {}
for i in L:
    D[i] = D.get(i, 0) + 1

# create list of elements with odd number of occurances
X = []
for i in D:
    if D[i] % 2:
        X.append(i)

# print elements
print(X[0], X[1])
