n, k = map(int, input().split())
a = [int(x) for x in input().split()]

a.sort()

res = 0
m = 0
i = 0
while i < n:
    cnt = 1
    j = i + 1
    while j < n and a[j] - a[i] <= 5:  # 5 is the distance
        cnt += 1
        j += 1

    if cnt < k:
        res += cnt
        m = max(m, res)
        res -= 1
    else:
        res += k
        m = max(m, res)
    i = j

print(m)
