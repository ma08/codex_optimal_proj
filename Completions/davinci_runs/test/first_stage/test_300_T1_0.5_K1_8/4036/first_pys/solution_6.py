

# SOLUTION
# https://codeforces.com/contest/1081/submission/45744501

n, k = map(int, input().split())
a = [1] * k
while sum(a) < n:
  a[0] += 1
  a.sort()
  a.reverse()
if sum(a) != n:
  print("NO")
else:
  print("YES")
  print(*a)