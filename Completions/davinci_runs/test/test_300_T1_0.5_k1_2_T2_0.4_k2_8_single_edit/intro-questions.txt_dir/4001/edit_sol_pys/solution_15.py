

# read input
N, K = map(int, input().split())
L = list(map(int, input().split())

# sort list
L.sort()

# create list of numbers
X = []
for i in D:
    if D[i] % 2:
        X.append(i)

# print numbers
print(X[0], X[1])
