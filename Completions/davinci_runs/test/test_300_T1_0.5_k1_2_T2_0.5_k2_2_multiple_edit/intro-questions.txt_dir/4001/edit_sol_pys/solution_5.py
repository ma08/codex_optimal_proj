

# read N, and create empty list
L = []

N = int(input())
# read list
for i in range(N):
    L.append(int(input()))

# create dictionary for numbers and count them
D = {}
for i in L:
    D[i] = D.get(i, 0) + 1

# create list of numbers that occur odd times
X = []
for i in D:
    if D[i] % 2:
        X.append(i)

# print odd numbers
print(X[0], X[1])
