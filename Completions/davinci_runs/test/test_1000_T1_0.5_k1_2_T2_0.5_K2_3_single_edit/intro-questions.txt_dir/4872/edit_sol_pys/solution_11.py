
n = int(input())
d = list(map(int, input().split()))

cleanup = 0
dirty = 0
for i in range(n):
    if dirty >= 20:
        while dirty >= 20:
            cleanup += 1
            dirty -= 20
    dirty += (d[i] - 1)

if dirty >= 20:
    while dirty >= 20:
        cleanup += 1
        dirty -= 20

print(cleanup)
