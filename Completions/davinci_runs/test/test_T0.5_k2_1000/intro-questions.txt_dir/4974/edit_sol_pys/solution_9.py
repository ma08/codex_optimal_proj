
n, m = map(int, input().split())
a = list(map(int, input().split()))

for i in range(m):
    b, c = map(int, input().split())
    for j in range(b):
        a[j] = c
    a.sort()

print(sum(a))
