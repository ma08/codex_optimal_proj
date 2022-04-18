
n = int(input())
cleanup = 0
d = list(map(int, input().split()))

dirty = 0
for i in range(n):
    while dirty >= 20:
        cleanup += 1
        dirty -= 20
    dirty += d[i] - 1

while dirty >= 20:
    cleanup += 1
    dirty -= 20

print(cleanup)
