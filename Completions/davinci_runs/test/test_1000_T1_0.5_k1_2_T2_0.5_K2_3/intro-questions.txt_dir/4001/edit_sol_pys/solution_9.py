
# read N

N = int(input())
# read list
L = list(map(int, input().split()))

# create dictionary for numbers and count
D = {}  # key:number, value:count
for num in L:
    D[num] = D.get(num, 0) + 1

# create list of numbers
X = []
for num in D:
    if D[num] % 2:
        X.append(num)

# print numbers
print(X[0], X[1])
