
n, x = map(int, input().split())
a = list(map(int, input().split()))
print(sum(max(a[i]+a[i+1]-x, 0) for i in range(n-1)))
