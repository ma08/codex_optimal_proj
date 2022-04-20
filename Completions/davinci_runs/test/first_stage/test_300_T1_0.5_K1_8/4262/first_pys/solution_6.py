

"""
条件を満たす順列の数はN!通り。
順列P,Qはそれぞれa,b番目に小さい順列である。
この条件を満たすa,bの組み合わせはN!通りある。
このうち、a-bが最小になる組み合わせを求める。
"""

# N!通りの全ての順列を生成。
# それぞれの順列に対して、順列P,Qがそれぞれa,b番目に小さい順列であるかを判定。
# それぞれの順列について、a-bを計算。
# a-bが最小になる組み合わせを求める。

# 入力
N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# 順列の生成
permutations = [list(i) for i in permutations(range(1, N+1))]

# a-bを計算
ab_list = []
for i in permutations:
    a = b = 0
    for j in range(N):
        if i[j] < P[j]:
            a += 1
        if i[j] < Q[j]:
            b += 1
    ab_list.append(abs(a-b))

# a-bが最小になる組み合わせを求める
print(min(ab_list))