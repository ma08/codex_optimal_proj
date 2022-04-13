N, K = map(int, input().split())
h = list(map(int, input().split()))
print(min(h[i+K-1] - h[i] for i in range(N-K+1)))
