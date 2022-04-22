

# 全ての数字が入る可能性があるとする
possible_numbers = [str(i) for i in range(10)]

# 入力
# ex.
# 2 3
# 1 9
# 2 1
# 2 0
n, m = 2, 3
q = [[1, 9], [2, 1], [2, 0]]

# 全ての桁について、c_iが入る可能性のある数字を決める
for i in range(m):
    # s_i-1: s_i番目の桁を表す
    # c_i: 桁に入る数字
    s_i, c_i = q[i][0] - 1, str(q[i][1])
    # possible_numbers[s_i]には、s_i番目の桁に入る可能性のある数字が入っている
    # ここでは、c_iをs_i番目の桁に入る可能性のある数字に追加し、
    # それ以外の数字を削除する
    possible_numbers[s_i] = c_i
    for j in range(10):
        if str(j) != c_i:
            possible_numbers[s_i] = possible_numbers[s_i].replace(str(j), '')

# 全ての桁について、c_iが入る可能性のある数字を決めたので、
# それらを組み合わせて、n桁の数字を作る
# possible_numbers = [['9'], ['1', '0']]
# itertools.product(*possible_numbers)は、以下のようなリストを返す
# [('9', '1'), ('9', '0')]
possible_numbers = ['9', '1', '0']
print(possible_numbers)
print(list(itertools.product(*possible_numbers)))
