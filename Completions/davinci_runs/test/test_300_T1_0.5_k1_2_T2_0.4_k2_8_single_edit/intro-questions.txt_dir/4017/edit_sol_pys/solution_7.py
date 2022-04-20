
n = int(input())
a = list(map(int, input().split()))

def is_good(a):
    return any(a[i] == sum(a[:i]) + sum(a[i+1:]) for i in range(len(a)))

res = []
for i in range(n):
    if is_good(a[:i] + a[i+1:]):
        res.append(i+1)

print(len(res))
print(*res)
