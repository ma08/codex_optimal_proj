

n,k = map(int, input().split())
h = list(map(int, input().split()))
h.sort()
print(min(h[i+k-1] - h[i] for i in range(n-k+1)))
