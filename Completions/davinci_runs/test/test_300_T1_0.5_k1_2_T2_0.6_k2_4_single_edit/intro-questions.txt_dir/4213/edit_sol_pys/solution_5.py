

N = int(input())
A = list(map(int, input().split()))

# 累積和を求める
sum_A = [0] * (N + 1)
for i in range(N):
    sum_A[i + 1] = sum_A[i] + A[i]
