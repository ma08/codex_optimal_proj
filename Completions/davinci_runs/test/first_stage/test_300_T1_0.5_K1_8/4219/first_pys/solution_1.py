
import math

N = int(input())
A = []
x = []
y = []
for i in range(N):
    Ai = int(input())
    A.append(Ai)
    xi = []
    yi = []
    for j in range(Ai):
        xij, yij = map(int, input().split())
        xi.append(xij)
        yi.append(yij)
    x.append(xi)
    y.append(yi)

# 3**N(個人)のbit全探索
ans = 0
for bit in range(1 << N):
    # bitのiビット目が1かどうか
    # 1が立っている人は嘘つきとする
    flag = True
    for i in range(N):
        if bit & (1 << i):
            continue
        # i番目の人が嘘つきでないと仮定して、
        # 全ての証言が正しいかを確認する
        for j in range(A[i]):
            # x[i][j]番目の人が嘘つきかどうか
            k = x[i][j] - 1
            if (bit & (1 << k)) != y[i][j]:
                flag = False
    if flag:
        ans = max(ans, N - bin(bit).count("1"))
print(ans)