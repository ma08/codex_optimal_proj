
n = int(input())
a = list(map(int, input().split()))

s = sum(a)

def is_good(b):
    for i in range(len(b)):
        if b[i] == sum(b[:i]) + sum(b[i+1:]):
            return i
    return -1

res = []
for i in range(n):
    if is_good(a[:i] + a[i+1:]):
        res.append(i+1)

print(len(res))
print(*res)
