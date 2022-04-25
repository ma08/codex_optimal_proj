L, R = map(int, input().split())

if R - L > 2019:
  print(0)
else:
  l = L % 2019
  r = R % 2019
  if l < r:
    l, r = r, l
  min_val = 2019
  for i in range(r+1, l):
    for j in range(i+1, l+1):
      min_val = min(min_val, i * j % 2019)
  print(min_val)
