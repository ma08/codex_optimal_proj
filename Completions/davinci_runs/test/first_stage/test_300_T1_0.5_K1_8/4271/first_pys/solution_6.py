

# N
N = int(input())
# A_1 A_2 ... A_N
A = list(map(int, input().split()))
# B_1 B_2 ... B_N
B = list(map(int, input().split()))
# C_1 C_2 ... C_{N-1}
C = list(map(int, input().split()))

# 全部の品を食べるとすると、最大でN回食べることができる。
# 全部の品を食べるとすると、最大でN回食べることができる。
# ピッタリN回食べるとすると、Aの順番が最高になる。
# ここで、A[0]はA[N-1]を食べた後に食べることができないので、A[0]を食べるときはC[N-1]を加算できない。
# そこで、A[0]を食べるときは、A[N-1]とC[N-1]を食べないこととする。
# これで、A[0]を食べるときはC[N-1]を加算できない。
# これで、A[0]を食べるときはC[N-1]を加算できない。
# これで、最高になるAの順番を求めることができる。
# これで、最高になるAの順番を求めることができる。
# これで、最高になるAの順番を求めることができる。
# これで、最高になるAの順番を求めることができる。
# これで、最高になるAの順番を求めることができる。
# これで、最高になるAの順番を求めることができる。
# これで、最高になるAの順番を求めることができる。
# これで、最高になるAの順番を求めることができる。
# これで、最高になるAの順番を求めることができる。

# 食べる順番を決める
order = []
order.append(A[0])
for i in range(1, N):
    # A[i-1]よりも大きいものを探す
    for j in range(N):
        if A[j] > A[i-1]:
            order.append(A[j])
            break

# 全部の食べ物が食べられたかどうか確認する
if len(order) != N:
    print("Not found")
    exit()

# 満足度の合計を計算する
satisfaction = 0
for i in range(N):
    satisfaction += B[order[i]-1]
    if i < N-1:
        satisfaction += C[order[i]-1]

print(satisfaction)