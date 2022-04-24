# 入力

n = int(input())
a = list(map(int,input().split()))

ans = [-1] * n
count = 0

for i in range(n):
    ans[a[i]-1] = count
    count = count + 1

print(' '.join(map(str,ans)))
