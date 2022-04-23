

# read N, M
N, M = map(int, input().split())
# read list of N numbers
L = list(map(int, input().split()))[:N]

# create dictionary for numbers and their count
D = {}
for i in L:
    D[i] = D.get(i, 0) + 1

# create list of odd numbers and their count
X = [] # list of numbers
Y = [] # list of counts
for i in D:
    if D[i] % 2 == 1:
        Y.append(D[i])
        X.append(i)

# print odd numbers and their count
for i in range(len(X)):
    print(X[i], Y[i])
