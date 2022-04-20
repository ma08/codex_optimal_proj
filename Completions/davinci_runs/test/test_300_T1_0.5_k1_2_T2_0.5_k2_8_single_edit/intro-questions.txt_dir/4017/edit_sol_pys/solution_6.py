

n = int(input())
a = list(map(int, input().split()))

s = sum(a)

def is_good(a, s):
    for i in range(len(a)):
        if a[i] == s - a[i]:
            return True
    return False

res = []
for i in range(n):
    if is_good(a[:i] + a[i+1:], s - a[i]):
        res.append(i+1)

print(len(res))
print(*res)
