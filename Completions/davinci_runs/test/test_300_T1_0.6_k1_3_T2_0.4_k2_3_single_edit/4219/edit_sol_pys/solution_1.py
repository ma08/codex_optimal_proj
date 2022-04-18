
n, m = map(int, input().split())
a = [0] * n
for i in range(m):
    a[int(input()) - 1] += 1
print(a.count(0))
