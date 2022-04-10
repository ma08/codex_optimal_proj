

n,m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

count = 0

for i in range(n):
    if a[i] < m:
        continue
    else:
        break

for j in range(n-1, -1, -1):
    if a[j] > m:
        continue
    else:
        break

for k in range(i, j+1):
    count += k-i+1

print(count)