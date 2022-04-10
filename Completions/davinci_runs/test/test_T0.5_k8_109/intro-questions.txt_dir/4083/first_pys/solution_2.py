

# Solution

n, k = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

def check(x):
    return sum(1 for i in a if i >= x) >= k

l = 1
r = max(a)

while l < r:
    m = (l + r) // 2
    if not check(m):
        l = m + 1
    else:
        r = m

print(l - 1)