
n = int(input())
f = list(map(int, input().split()))

# find the first 0
idx = f.index(0)

# find the next non-zero
for i in range(idx+1, n):
    if f[i] != 0:
        f[idx] = f[i]
        break

# fill the rest of the zeros
for i in range(idx+1, n):
    if f[i] == 0:
        for j in range(1, n+1):
            if j not in f:
                f[i] = j
                break

print(*f)
