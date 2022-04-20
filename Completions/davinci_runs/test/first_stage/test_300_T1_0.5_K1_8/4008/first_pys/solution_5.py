

n, k = map(int, input().split())
a = list(map(int, input().split()))

if k > n:
  print("NO")
  exit()

c = [0] * n

for i in range(n):
  for j in range(1, k + 1):
    if c[i] == 0:
      c[i] = j
      for x in range(i):
        if a[x] == a[i] and c[x] == j:
          c[i] = 0
          break

if 0 in c:
  print("NO")
else:
  print("YES")
  print(*c)