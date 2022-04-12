import math
n,k = map(int, input().split())
a = list(map(int, input().split()))
if k == 1:
    print(max(a))
else:
    max_sum = sum(a[:k])
    curr_sum = max_sum
    for i in range(k,n):
        curr_sum += a[i] - a[i-k]
        max_sum = max(max_sum, curr_sum)
    print(math.ceil(max_sum/k))
