
# read number of test cases
T = int(input())

# iterate over test cases
for i in range(T):
    # read N
    N = int(input())
    # read list
    L = list(map(int, input().split()))

    # create dictionary for numbers
    D = {}
    for j in L:
        D[j] = D.get(j, 0) + 1

    # create list of numbers
    X = []
    for j in D:
        if D[j] % 2:
            X.append(j)

    # print numbers
    print(X[0], X[1])
