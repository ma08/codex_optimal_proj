

import sys

sys.setrecursionlimit(10 ** 6)

n, k = map(int, input().split())

segments = [0] * n
segments_by_end = [0] * n
for _ in range(n):
    l, r = map(int, input().split())
    segments[i] = (l, r)
    segments_by_end[i] = (r, i)

# print(segments)

segments_by_end.sort()
# print(segments_by_end)


def get_next_segment(segments, i):
    l, r = segments[i]
    j = i + 1
    while j < n and segments[j][0] <= r:
        if segments[j][1] > r:
            r = segments[j][1]
        j += 1
    return (r, j - 1)


result = []

for i in range(n):
    l, r = segments[i]
    j = i + 1
    while j < n and segments[j][0] <= r:
        if segments[j][1] > r:
            r = segments[j][1]
        j += 1
    result.append((r - l + 1, i + 1))

# print(result)

result.sort(reverse=True)

# print(result)

result = [i for _, i in result]

# print(result)

cnt = 0

for i in result:
    l, r = segments[i - 1]
    if cnt + r - l + 1 <= k:
        cnt += r - l + 1
    else:
        break

print(len(result) - cnt)
print(*result[:len(result) - cnt])
