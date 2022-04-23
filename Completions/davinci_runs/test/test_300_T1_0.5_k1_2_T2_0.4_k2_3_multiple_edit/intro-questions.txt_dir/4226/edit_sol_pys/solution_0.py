n, m, x = map(int, input().split())
a = list(map(int, input().split()))


left = 0
right = 0

if y % 2 == 0 and x * 2 <= y and y <= x * 4:  # 偶数で、xの2倍以上、xの4倍以下
    print('Yes')
else:
    print('No')
