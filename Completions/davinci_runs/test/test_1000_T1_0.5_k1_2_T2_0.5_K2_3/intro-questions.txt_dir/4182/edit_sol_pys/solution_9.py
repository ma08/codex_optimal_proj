

n, m, x, y = map(int, input().split())
x_list = [int(i) for i in input().split()]
y_list = [int(i) for i in input().split()]

x_list.sort()  # x_listをソート
y_list.sort()  # y_listをソート

if x_list[-1] >= y_list[0]:  # x_listの最大値がy_listの最小値以上の場合は壁がある
    print('War')
else:
    print('No War')
