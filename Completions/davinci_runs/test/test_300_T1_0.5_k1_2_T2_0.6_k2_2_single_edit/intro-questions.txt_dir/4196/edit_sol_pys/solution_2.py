
# 入力
N = int(input())
A = list(map(int, input().split()))

a = []
for i in range(N):
    a.append(i)

# 初期化
ans = 0

# 組み合わせを全部試す
for i in range(2**N):
    # 集合を初期化
    S = []
    for j in range(N):
        # 集合Sに値を追加
        if (i >> j) & 1:
            S.append(A[j])

    # 集合内の最大公約数
    tmp = 0
    for j in range(len(S)):
        tmp = gcd(tmp, S[j])

    # 集合内の最大公約数がansより大きければ更新
    ans = max(tmp, ans)

# 解答
print(ans)
