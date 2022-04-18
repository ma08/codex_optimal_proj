

n = int(input())  # 入力

d_list = []
for i in range(n):  # 入力
    d_list.append(int(input()))

d_set = set(d_list)  # setを作成

print(len(d_set))  # 出力
