n = int(input())
a = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i] != a[j] and a[j] != a[k] and a[k] != a[i] and a[i] + a[j] > a[k]:
                ans += 1
print(ans)
