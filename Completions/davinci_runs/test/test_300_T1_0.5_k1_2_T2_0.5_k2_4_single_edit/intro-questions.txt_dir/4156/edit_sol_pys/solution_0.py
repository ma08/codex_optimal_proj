
n, w = map(int, input().split())
a = list(map(int, input().split()))

i = 0
ans = 0
j = 0

for i in range(n):
    if a[i] > w or a[i] < -w:
        ans = 0
        break
    j += a[i]
    if j > w or j < 0:
        ans = 0
        break

if i == n-1:
    ans = w-j+1

print(ans)
