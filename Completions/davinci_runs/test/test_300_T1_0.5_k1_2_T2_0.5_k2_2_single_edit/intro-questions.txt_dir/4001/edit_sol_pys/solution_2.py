
# read N
N = int(input())
# read list
L = list(map(int, input().split()))

# print numbers with odd count
for i in L:
    if L.count(i) % 2:
        print(i, end=' ')
