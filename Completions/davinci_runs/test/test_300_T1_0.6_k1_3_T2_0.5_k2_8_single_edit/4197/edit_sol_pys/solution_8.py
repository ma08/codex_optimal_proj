

n = int(input())
a = list(map(int,input().split()))

#print(n)
#print(a)

ans = [-1] * n
count = 0

for i in range(n):
    if a[i] - 1 == i:
        ans[a[i]-1] = count
        count = count + 1

print(' '.join(map(str,ans)))
