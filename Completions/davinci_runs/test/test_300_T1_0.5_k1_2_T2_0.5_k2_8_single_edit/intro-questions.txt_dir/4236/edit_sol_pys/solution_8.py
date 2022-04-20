
n, m = map(int, input().split())

segments = []
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))

res = []
for i in range(1, m + 1):
    for segment in segments:
        if i in range(segment[0], segment[1] + 1):
            break
    else:
        res.append(i)  # только если не было досрочного выхода из цикла

print(len(res))
print(*res)
