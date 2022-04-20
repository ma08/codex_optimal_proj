

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 食べていく順番にBとCを並び替える(Aは食べる順番のインデックスが書かれている)
B = [B[A[i]-1] for i in range(N)]
C = [C[A[i]-1] for i in range(N-1)]

# 合計を計算
total = sum(B) + sum(C)

# 直前に食べた料理と同じものを食べたときのポイントを減算する
for i in range(N-2):
    if A[i] == A[i+1]:
        total -= C[i]

print(total)
