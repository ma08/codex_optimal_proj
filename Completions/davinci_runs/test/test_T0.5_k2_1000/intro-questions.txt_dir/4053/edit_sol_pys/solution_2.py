# https://codeforces.com/contest/1326/problem/C

n = int(input())  # number of elements
a = list(map(int, input().split()))  # elements
q = int(input())  # number of queries
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a[query[1]-1] = query[2]
    else:
        print(a[query[1]-1] ^ a[query[2]-1])
