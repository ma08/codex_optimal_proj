
L, R = map(int, input().split())

if R - L > 2019:
  print(0)
else:
  l = L % 2019  # Lの2019で割った余り
  r = R % 2019  # Rの2019で割った余り
  if l < r:  # lがrより小さい場合は、lとrを入れ替える
    l, r = r, l  # lとrを入れ替える
  min_val = 2019
  for i in range(r+1, l):  # r+1～l-1までループ
    for j in range(i+1, l+1):  # i+1～lまでループ
      min_val = min(min_val, i * j % 2019)  # min_valを更新
  print(min_val)
