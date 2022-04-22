

n = int(input())
a = list(map(int, input().split()))

# 与えられた配列をソートする
sorted_a = sorted(a)

# 与えられた配列をソートした配列をコピーする
tmp = sorted_a.copy()

# 最大値を取り出す
max_value = max(a)

# 最大値を取り出した配列を作る
a_without_max_value = [x for x in a if x != max_value]

# 記憶した数字が2つ以上あるなら、NOを出力する
# そうでなければ、YESを出力する
if len(diff_index) > 2:
    print('NO')
else:
    print('YES')
