
n = int(input())
a = list(map(int, input().split()))  # input list

l = [0] * n  # list of indexes

for i in range(n):
    l[a[i]-1] = i+1

for i in range(n):
    if i == n-1:
        print(l[i])
    else:
        print(l[i], end=' ')
