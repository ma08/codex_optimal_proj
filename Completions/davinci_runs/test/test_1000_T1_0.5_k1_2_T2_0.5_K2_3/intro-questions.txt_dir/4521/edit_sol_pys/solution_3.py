n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

x = sorted([x[i] + v[i] for i in range(n)])

d = 0
for i in range(n - 1):
    d += x[i + 1] - x[i]

print(d)
