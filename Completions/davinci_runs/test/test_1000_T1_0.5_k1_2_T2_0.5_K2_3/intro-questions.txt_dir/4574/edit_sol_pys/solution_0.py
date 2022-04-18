import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n - 3):
    for j in range(i + 1, n - 2):
        for k in range(j + 1, n - 1):
            for l in range(k + 1, n):
                if a[i] != a[j] != a[k] != a[l]:
                    ans = max(ans, a[i] * a[j])

print(ans)
