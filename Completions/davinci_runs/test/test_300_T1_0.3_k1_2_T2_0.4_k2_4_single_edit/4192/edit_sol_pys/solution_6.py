

d, t, s = map(int, input().split())  # d:距離, t:時間, s:速度

if d / s <= t:
    print('Yes')
else:
    print('No')
