

# read N, M
N, M = map(int, input().split())

# read list
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# create dictionary for numbers and count for A
D = {}  # key:number, value:count of A
for num in A:
    D[num] = D.get(num, 0) + 1  # default value = 0

X = []  # list of numbers
for num in D:
    if D[num] % 2:  # if odd
        X.append(num)

for num in B:
    if num in D:
        if D[num] % 2:  # if odd
            print(num)
            break
