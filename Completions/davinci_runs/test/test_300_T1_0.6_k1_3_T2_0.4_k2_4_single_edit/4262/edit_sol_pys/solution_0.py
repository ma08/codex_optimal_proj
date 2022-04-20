
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# 全部書き出して、何番目に来るかを確かめる
all_permutations = [i for i in range(1, N+1)]

# P, Q が何番目に来るかを確かめる
P_index = all_permutations.index(P)
Q_index = all_permutations.index(Q)

# 差を求める
diff = abs(P_index - Q_index)

# 結果を出力
print(diff)
