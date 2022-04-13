n, k = map(int, input().split())
segments = []
for _ in range(n):
    segments.append(tuple(map(int, input().split())))
segments.sort()
result = []
for i in range(n):
    l, r = segments[i]
    j = i + 1
    while j < n and segments[j][0] <= r:
        if segments[j][1] > r:
            r = segments[j][1]
        j += 1
    result.append((r - l + 1, i + 1))
result.sort(reverse=True)
result = [i for _, i in result]
cnt = 0
for i in result:
    l, r = segments[i - 1]
    if cnt + r - l + 1 <= k:
        cnt += r - l + 1
    else:
        break
print(len(result) - cnt)
print(*result[:len(result) - cnt])
