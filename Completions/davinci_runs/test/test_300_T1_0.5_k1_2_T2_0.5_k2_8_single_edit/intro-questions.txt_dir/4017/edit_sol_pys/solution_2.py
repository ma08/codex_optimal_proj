

n = int(input())
a = list(map(int, input().split()))

s = sum(a)

def is_good(a):
    for i in range(len(a)):
        if a[i] == sum(a[:i]) + sum(a[i+1:]):
            return True
    return False

res = []
for i in range(n):
    if is_good(a[:i] + a[i+1:]):
        res.append(i+1)

print(len(res))



print(*res)
