
n = int(input())
a = list(map(int, input().split()))

odd = 0
even = 0

for i in range(n):
    if i % 2 == 0:
        even += a[i]
    else:
        odd += a[i]

ans = 0
for i in range(n):
    if i % 2 == 0:
        if odd - a[i] == even:
            ans += 1
    else:
        if even - a[i] == odd:
            ans += 1

print(ans)
