

# read number of test cases
T = int(input())

# iterate over test cases
for _ in range(T):
    # read N
    N = int(input())
    # read list
    L = list(map(int, input().split()))

# create list of numbers
X = []
for i in D:
    if D[i] % 2:
        X.append(i)

# print numbers
print(X[0], X[1])
