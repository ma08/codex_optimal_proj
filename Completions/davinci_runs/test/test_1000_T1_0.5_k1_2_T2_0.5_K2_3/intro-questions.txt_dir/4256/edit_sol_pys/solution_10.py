n,m,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
a_sum = [0]
b_sum = [0]


for i in range(n):
    a_sum.append(a_sum[i] + a[i])

for i in range(m):
    b_sum.append(b_sum[i] + b[i])

j = m

for i in range(n+1):
    if a_sum[i] > k:
        break
    while b_sum[j] > k - a_sum[i]:
        j -= 1
    ans = max(ans,i+j)

print(ans)
