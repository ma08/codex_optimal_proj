
from bisect import bisect_left

n, m = map(int, input().split())

segments = []
for i in range(n):
    segments.append(list(map(int, input().split())))

# print(segments)

segments.sort(key=lambda x: x[0])

# print(segments)

res = []
for i in range(1, m + 1):
    if i not in [seg[0] for seg in segments] and i not in [seg[1] for seg in segments]:
        res.append(i)

print(len(res))
print(*res)
