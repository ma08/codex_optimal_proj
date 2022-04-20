

n = int(input())
a = list(map(int, input().split()))

a.sort()

ans = [a[-1]]

for i in range(n - 1, 0, -1):
    if a[i] % 3 == 0:
        ans.append(a[i - 1])
    else:
        ans.append(a[i])

print(*ans[::-1])