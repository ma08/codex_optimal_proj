

n = int(input())
x = [int(i) for i in input().split()]

x.sort()

l = 0
r = 1000000000

while l < r:
    m = (l + r) // 2
    c = 0
    for i in x:
        c += abs(m - i)
    if c <= n:
        r = m
    else:
        l = m + 1

c = 0
for i in x:
    c += abs(l - i)

print(c // 2)