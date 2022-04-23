
n = int(input())
h = list(map(int, input().split()))

ans = 0
i = 0
while i < n:
    if h[i] > 0:
        ans += 1
        for j in range(i+1, n):
            if h[j] > 0:
                h[j] -= 1
            else:
                i = j
                break
        else:
            i = n

print(ans)
