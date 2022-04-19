
n = int(input())
a = list(map(int, input().split()))

s = sum(a)

res = []
for i in range(n):
    if s - a[i] == sum(a[:i]) + sum(a[i+1:]):
        res.append(i+1)

print(len(res))
print(*res)
