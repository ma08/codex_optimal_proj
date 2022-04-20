

nm = input().split()
n = int(nm[0])
m = int(nm[1])

foods = [0] * m

for i in range(n):
    k = input().split()
    k = k[1:]
    for j in range(len(k)):
        foods[int(k[j]) - 1] += 1

ans = 0
for i in range(m):
    if foods[i] == n:
        ans += 1

print(ans)