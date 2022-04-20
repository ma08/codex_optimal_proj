
n, m, x, y = map(int, input().split())  # 入力
x_list = [int(i) for i in input().split()]  # 入力
y_list = [int(i) for i in input().split()]  # 入力
x_list.sort()  # 昇順ソート
y_list.sort()  # 昇順ソート
if x_list[-1] >= y_list[0]:  # 判定
    print('War')  # 表示
else:  # 判定
    print('No War')  # 表示
