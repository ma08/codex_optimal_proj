
# SOLUTION
n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

x = [x[i] + v[i] for i in range(len(x))]

x.sort()

d = 0
for i in range(len(x) - 1):
    d += x[i + 1] - x[i]

print(d)
