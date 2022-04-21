

n = int(input())
a = list(map(int, input().split()))

s = sum(a)

def is_good(a):
    for i in range(1, len(a)):
        if a[i-1] > a[i]:
            return False
    return True

res = []
for i in range(n):
    if is_good(a[:i] + a[i+1:]):
        res.append(i+1)

print(len(res))
print(*res)
