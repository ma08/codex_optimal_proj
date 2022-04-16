#

n,k = map(int, input().split())
a = list(map(int, input().split()))

max_sum = sum(a[:k])
curr_sum = max_sum
for i in range(k,n):
    curr_sum += a[i] - a[i-k]
    max_sum = max(max_sum, curr_sum)

print(max_sum/k)
