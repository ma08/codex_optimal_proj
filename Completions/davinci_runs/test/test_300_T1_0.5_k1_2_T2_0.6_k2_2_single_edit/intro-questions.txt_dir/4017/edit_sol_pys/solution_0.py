n = int(input())
a = [int(i) for i in input().split()]


def is_good(a, i):
    return a[i] == sum(a[:i]) + sum(a[i+1:])

res = []
for i in range(n):
    if is_good(a, i):
        res.append(i+1)

print(len(res))
print(*res)
