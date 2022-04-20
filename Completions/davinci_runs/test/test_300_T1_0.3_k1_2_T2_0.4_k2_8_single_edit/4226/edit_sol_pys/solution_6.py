

x = int(input())
y = int(input())

if y % 2 == 0 and (2 * x + 4 * (y // 4 - x)) == y and x >= 0 and y >= 0:
    print('Yes')
else:
    print('No')
