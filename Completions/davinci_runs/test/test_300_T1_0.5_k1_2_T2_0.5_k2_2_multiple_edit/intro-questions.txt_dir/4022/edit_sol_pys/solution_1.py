
# Solution

n = int(input())

x = [0] * n
y = [0] * n

for i in range(n):
    a, b = map(int, input().split())
    x[i] = a
    y[i] = b

x.sort()
y.sort()

print(y[-1] - x[0])
