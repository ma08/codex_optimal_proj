

x, y = map(int, input().split())

if y % 2 == 0 and x * 2 <= y <= x * 4:  # 偶数で、xの2倍以上、xの4倍以下
    print('Yes')
else:
    print('No')
