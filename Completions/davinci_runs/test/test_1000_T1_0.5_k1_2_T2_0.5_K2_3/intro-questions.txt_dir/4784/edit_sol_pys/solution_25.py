

x = int(input())
n = int(input())

p = [0] * (n + 1)
for i in range(n):
    p[i] = int(input())

p[n] = x
for i in range(n - 1, -1, -1):
    p[i] = p[i + 1] - p[i]

print(p[0])
