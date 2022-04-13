
n = int(input())  # 1行目

d_list = []
for i in range(n):
    d_list.append(int(input()))  # 2行目以降
d_set = set(d_list)
print(len(d_set))
