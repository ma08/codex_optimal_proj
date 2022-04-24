

# read N
N = int(input())
# read numbers
L = input().split()

# create dictionary for numbers and count them
D = {}
for i in L:
    D[i] = D.get(i, 0) + 1 # get(key, default)

# create list of numbers that occur odd times
X = []
for i in D:
    if D[i] % 2: # check if number occurs odd times
        X.append(i)

# print odd numbers
print(X[0], X[1])
