

N = int(input())
P = list(map(int, input().split())) # P の順列
Q = list(map(int, input().split())) # Q の順列

# 全部書き出して、何番目に来るかを確かめる
all_permutations = [i for i in range(1, N+1)] # 全部の数字を書き出す

# P, Q が何番目に来るかを確かめる
P_index = all_permutations.index(P) # P の順列が何番目に来るか
Q_index = all_permutations.index(Q) # Q の順列が何番目に来るか

# 差を求める
diff = abs(P_index - Q_index)

# 結果を出力
print(diff)
