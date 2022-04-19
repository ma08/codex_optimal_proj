

n, m, x, y = map(int, input().split())
x_list = [int(i) for i in input().split()]
y_list = [int(i) for i in input().split()]

x_list.sort()
y_list.sort()

if x >= y_list[0] or x_list[-1] >= y:
    print('War')
else:
    print('No War')
