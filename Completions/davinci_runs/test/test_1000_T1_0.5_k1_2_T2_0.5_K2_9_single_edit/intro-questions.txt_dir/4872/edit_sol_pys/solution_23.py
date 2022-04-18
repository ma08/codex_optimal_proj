

n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(m):
    ans += a[i]

while dirty >= 20:
    cleanup += 1
    dirty -= 20

print(cleanup)
