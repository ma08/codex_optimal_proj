
n, m = map(int, input().split())

segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

segments.sort(key=lambda x: x[0])

# print(segments)

res = []
for i in range(1, m + 1):
    if i not in [seg[0] for seg in segments]:
        if i not in [seg[1] for seg in segments]:
            res.append(i)

print(len(res))
print(*res)
