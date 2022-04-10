

n = int(input())
f = list(map(int, input().split()))

# find the first 0
for i in range(n):
    if f[i] == 0:
        f[i] = f[f[i] - 1]
        break

# find the second 0
for i in range(n):
    if f[i] == 0:
        f[i] = f[f[i] - 1]
        break

# find the rest of the 0s
for i in range(n):
    if f[i] == 0:
        f[i] = f[f[i] - 1]

print(*f)