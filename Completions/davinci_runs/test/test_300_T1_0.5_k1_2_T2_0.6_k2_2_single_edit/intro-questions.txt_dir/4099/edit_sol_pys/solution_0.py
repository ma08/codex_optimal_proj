N, K, M = map(int, input().split())
A = list(map(int, input().split()))  # リスト内包表記

# N, K, M = map(int, input().split())
# A = list(map(int, input().split()))  # リスト内包表記

# sumA = sum(A)
# avg = sumA / N

sum_A = sum(A)
avg = sum_A / N

if avg >= M:
    print(0)
    exit()

if K <= M:
    print(-1)
    exit()

print(M*N - sum_A)
