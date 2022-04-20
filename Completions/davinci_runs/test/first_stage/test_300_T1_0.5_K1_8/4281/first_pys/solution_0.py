

n = int(input())
x = list(map(int, input().split()))

x_min = [0]*(n+2)
x_max = [0]*(n+2)

for i in range(n):
    x_min[x[i]] += 1
    x_max[x[i]] += 1

x_min[1] -= 1
x_min[n] -= 1

for i in range(1, n+1):
    x_min[i] += x_min[i-1]

for i in range(n, 0, -1):
    x_max[i] += x_max[i+1]

print(max(x_min), max(x_max))