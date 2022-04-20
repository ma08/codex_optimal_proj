
# read N
N = int(input())
# read list
L = list(map(int, input().split()))

# create dictionary for numbers
D = {}
for i in L:
    D[i] = D.get(i, 0) + 1

# create list of numbers
X = [0, 0]
for i in D:
    if D[i] % 2 == 0:
        X[0] = i
    else:
        X[1] = i

# print numbers
print(X[0], X[1], sep=' ')
