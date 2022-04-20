

x, y = map(int, input().split())

if y % 2 == 0 and (2 * x + 4 * (y // 4 - x)) == y:
    print('Yes')
else:
    print('No')