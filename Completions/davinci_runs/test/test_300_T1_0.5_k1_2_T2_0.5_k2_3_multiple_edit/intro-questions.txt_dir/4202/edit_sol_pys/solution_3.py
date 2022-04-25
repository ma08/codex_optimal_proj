import sys
sys.setrecursionlimit(10**6)
L, R = map(int, input().split())

if R - L > 2019:
  print(0)
else:
  L = L % 2019
  R = R % 2019
  if L > R:
    L, R = R, L
  min_val = 2019 * 2019
  for i in range(L, R):
    for j in range(L, R):
      min_val = min(min_val, (i * j) % 2019)
  print(min_val % 2019)
