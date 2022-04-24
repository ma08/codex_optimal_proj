

N = int(input())
h = list(map(int, input().split()))

# h_i - iを求める
tmp = [0] * N
for i in range(N):
    tmp[i] = h[i] - (i+1)
tmp_dict = {}


# tmpの値が同じものはまとめる
# tmpの値をkeyとする辞書を作り、同じ値のものをまとめる
# まとめた後、番号の小さいものから順にまとめる
for i in range(N):
    tmp_dict.setdefault(tmp[i], []).append(i)

# 同じ値のものをまとめる
for key in tmp_dict.keys():
    tmp_dict[key].sort()

# 同じ値のものをまとめたものを出力する
ans = []
for key in tmp_dict.keys():
    tmp_list = []
    for i in range(len(tmp_dict[key])):
        if i == 0:
            tmp_list.append(tmp_dict[key][i])
            tmp_list.append(tmp_dict[key][i])
        elif tmp_dict[key][i-1] + 1 == tmp_dict[key][i]:
            tmp_list[1] = tmp_dict[key][i]
        else:
            ans.append(tmp_list)
            tmp_list = []
            tmp_list.append(tmp_dict[key][i])
            tmp_list.append(tmp_dict[key][i])
    ans.append(tmp_list)

print(len(ans))
