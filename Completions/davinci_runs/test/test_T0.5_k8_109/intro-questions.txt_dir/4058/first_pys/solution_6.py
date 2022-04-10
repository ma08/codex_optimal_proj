

n, r = map(int, input().split())
a = list(map(int, input().split()))

ans = 0

for i in range(n):
    if a[i] == 0:
        j = i - 1
        while j >= 0 and i - j <= r - 1:
            if a[j] == 1:
                ans += 1
                break
            j -= 1
        j = i + 1
        while j < n and j - i <= r - 1:
            if a[j] == 1:
                ans += 1
                break
            j += 1
        if j == n and j - i > r - 1:
            print(-1)
            exit()

print(ans)