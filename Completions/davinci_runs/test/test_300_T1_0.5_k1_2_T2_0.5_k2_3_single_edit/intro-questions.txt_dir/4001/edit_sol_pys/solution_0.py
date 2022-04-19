
# read N
N = int(input())
# read list of numbers
L = list(map(int, input().split()))[:N]

# create dictionary for numbers
D = {}
for i in L:
    D[i] = D.get(i, 0) + 1

# create list of numbers
X = []
for i in D:
    if D[i] % 2:
        X.append(i)
# sort list
X.sort()


# print numbers
print(X[0], X[1])
