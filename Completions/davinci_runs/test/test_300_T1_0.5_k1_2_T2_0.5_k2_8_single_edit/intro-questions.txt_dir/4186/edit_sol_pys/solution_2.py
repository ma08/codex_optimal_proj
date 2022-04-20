import math
n = int(input())
a = list(map(int, input().split()))
a.sort()


ans = 0
for i in range(n):
    for j in range(i + 1, n):
        x = a[i] + a[j]
        if x > a[-1]:
            break
        if x < a[-1]:
            l = j + 1
            r = n - 1
            while l < r:
                m = (l + r) // 2
                if a[m] < x:
                    l = m + 1
                else:
                    r = m
            ans += l - j - 1
        else:
            ans += 1

print(ans // 3)
