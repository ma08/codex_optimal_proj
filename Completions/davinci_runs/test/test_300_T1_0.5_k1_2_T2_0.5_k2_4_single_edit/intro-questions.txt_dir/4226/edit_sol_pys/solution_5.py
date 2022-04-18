

x, y, z = map(int, input().split())

if z % 2 == 0 and x * 2 <= z and z <= x * 4:
    print('Yes')
else:
    print('No')
