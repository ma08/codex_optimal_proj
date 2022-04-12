
n = int(input())  # 入力

d_list = []  # 入力された数字を格納するリスト
for i in range(n):
    d_list.append(int(input()))
d_set = set(d_list)  # 重複を削除したリスト
print(len(d_set))
