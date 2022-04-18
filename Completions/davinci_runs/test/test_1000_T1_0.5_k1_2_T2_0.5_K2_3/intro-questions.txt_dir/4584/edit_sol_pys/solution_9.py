

N = int(input())  # 入力される数
A = [int(i) for i in input().split()]  # 入力される数をリスト化

B = [0] * N  # 入力される数を格納するリスト

# 前の要素のインデックスを格納していく
for i in range(1, N):
    B[A[i - 1]] += 1

for i in range(N):
    print(B[i])
