

# read N and M
N = int(input())
M = int(input())
# read lists
A = list(map(int, input().split()))
B = list(map(int, input().split()))
L = list(map(int, input().split()))

# create dictionary for numbers A
D = {}
for i in A:
    D[i] = D.get(i, 0) + 1

# create list of numbers B
Y = []
for i in B:
    if D.get(i, 0) > 0:
        Y.append(i)

# print numbers Y
print(*Y)
