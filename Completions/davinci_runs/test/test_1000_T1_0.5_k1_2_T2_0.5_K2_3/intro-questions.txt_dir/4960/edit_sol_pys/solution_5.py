
#%%

n = int(input())
a = list(map(int, input().split()))
sum = 0

for i in range(n):
    for j in range(i, n):
        sum += a[i]*a[j]

print(sum)
