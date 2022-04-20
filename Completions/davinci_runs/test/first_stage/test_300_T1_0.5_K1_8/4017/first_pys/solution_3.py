

n = int(input())
a = list(map(int,input().split()))

s = sum(a)

count = 0
for i in range(n):
    if a[i]*(n-1) == s-a[i]:
        count+=1

print(count)
for i in range(n):
    if a[i]*(n-1) == s-a[i]:
        print(i+1,end=' ')