from itertools import accumulate

n = int(input())
a = list(map(int, input().split()))

acc = list(accumulate(a))

res = []
for i in range(n-1):
    if acc[i] == acc[-1] - acc[i]:
        res.append(i+1)

res = []
for i in range(n):
    if is_good(a[:i] + a[i+1:]):
        res.append(i+1)

print(len(res))
print(*res)
