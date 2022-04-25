import sys


n, m = map(int, sys.stdin.readline().split())

segments = []
for i in range(n):
    l, r = map(int, sys.stdin.readline().split())
    segments.append((l, r))

segments.sort(key=lambda x: x[0])

res = []
for i in range(1, m + 1):
    if i not in [seg[0] for seg in segments] and i not in [seg[1] for seg in segments]:
        res.append(i)

print(len(res))
print(*res)
