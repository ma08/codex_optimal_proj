
N, X = map(int, input().split())
A = list(map(int, input().split()))

count = 0
for i in range(N-1):
    if A[i] + A[i+1] > X: # 今日と明日のカロリーを足したものがxを超えていたら、それを減らす
        count += A[i] + A[i+1] - X
        A[i+1] -= A[i] + A[i+1] - X
print(count)
