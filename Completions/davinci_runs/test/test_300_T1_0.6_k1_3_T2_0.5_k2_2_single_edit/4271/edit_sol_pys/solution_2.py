

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# Aをインデックスの大きい順に並び替える
order_A = sorted(A, reverse=True)
# 食べていく順番にBとCを並び替える
B = [B[order_A.index(i)-1] for i in range(1,N+1)]
C = [C[order_A.index(i)-1] for i in range(1,N)]

# 合計を計算
total = sum(B) + sum(C)

# 直前に食べた料理と同じものを食べたときのポイントを減算する
for i in range(N-2):
    if order_A[i] == order_A[i+1]:
        total -= C[i]

print(total)

