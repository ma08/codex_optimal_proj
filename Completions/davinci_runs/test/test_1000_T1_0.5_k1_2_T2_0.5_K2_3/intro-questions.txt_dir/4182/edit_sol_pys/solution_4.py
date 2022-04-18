

N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

if x_list[-1] >= y_list[0]:  # x_listの最大値がy_listの最小値以上の場合は壁がある
    print('War')
else:
    print('No War')
