
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
        if b[i] > c[j]:
            ans += n - j
            break
print(ans)
