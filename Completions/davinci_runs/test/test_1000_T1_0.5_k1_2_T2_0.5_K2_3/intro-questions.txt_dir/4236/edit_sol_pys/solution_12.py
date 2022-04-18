
n, m = map(int, input().split())

segments = []
for i in range(n):
    left, right = map(int, input().split())
    segments.append((left, right))

segments.sort(key=lambda x: x[0])

# print(segments)

res = []
for i in range(1, m + 1):
    if i not in [seg[0] for seg in segments] and i not in [seg[1] for seg in segments] and segments[0][0] != 1:
        res.append(i)

print(len(res))
print(*res)
