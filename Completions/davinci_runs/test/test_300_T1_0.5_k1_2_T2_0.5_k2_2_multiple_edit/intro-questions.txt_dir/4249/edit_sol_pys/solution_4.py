n, m, k = map(int, input().split())

a = list(map(int, input().split())) + [0]
b = list(map(int, input().split())) + [0]

a.sort(reverse=True)
b.sort(reverse=True)

i = 0
j = 0
ans = 0

while i < n and j < m:
    if a[i] > b[j]:
        ans += 1
        i += 1
        j += 1
    else:
        if a[i] == b[j]:
            if k:
                ans += 1
                i += 1
                j += 1
                k -= 1
            else:
                ans += 1
                i += 1
        else:
            ans += 1
            j += 1
            k -= 1

    if k < 0:
        break

if k < 0:
    ans -= 1

print(ans)
