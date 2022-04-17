
# read N
N = int(input())
# read list of integers
L = list(map(int, input().split()))

# create dictionary for numbers with their frequencies
D = {}
for i in L:
    D[i] = D.get(i, 0) + 1

# create list of numbers with odd frequencies
X = []
for i in D:
    if D[i] % 2:
        X.append(i)

# print numbers
print(X[0], X[1])
