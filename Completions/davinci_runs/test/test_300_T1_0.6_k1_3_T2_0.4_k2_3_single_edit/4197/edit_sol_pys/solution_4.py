
n = int(input())
a = list(map(int,input().split()))

ans = [-1] * n

for i in range(n):
    count = 0
    for j in range(n):
        if a[j] > a[i]:
            count = count + 1
    ans[a[i]-1] = count

for i in range(n):
    ans[a[i]-1] = count
    count = count + 1

print(' '.join(map(str,ans)))
