
n = int(input())
d = list(map(int, input().split()))

cleanup = 0
dirty = 0
for i in range(n):
    while dirty >= 21:
        cleanup += 1
        dirty -= 21
    dirty += (d[i] - 1)

while dirty >= 21:
    cleanup += 1
    dirty -= 21

print(cleanup)
