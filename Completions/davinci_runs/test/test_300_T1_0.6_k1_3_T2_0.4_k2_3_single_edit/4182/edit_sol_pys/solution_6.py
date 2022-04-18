n, m, x, y = map(int, input().split())
x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

for i in range(x+1, y):
    if all(x_list[j] < i for j in range(n)) and all(y_list[j] >= i for j in range(m)):  # all()は全ての要素が真であるかを判定する関数
        print('No War')
        exit(0)
print('War')
