
n = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

c = list(map(int, input().split()))

a.sort()
b.sort()
c.sort()

ans = 0

for i in range(n):
    for j in range(n):
        if b[j] > a[i]:
            break
        for k in range(n):
            if c[k] > b[j]:
                break
            ans += 1

print(ans)
