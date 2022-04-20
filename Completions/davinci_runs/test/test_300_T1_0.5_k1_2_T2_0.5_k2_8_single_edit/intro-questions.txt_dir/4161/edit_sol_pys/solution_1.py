N, K = map(int, input().split())
a = list(map(int, input().split()))


print(sum(a[i] for i in range(N) if a[i] < K))
