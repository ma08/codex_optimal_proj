n, k = map(int, input().split())
a = list(map(int, input().split()))
print(sum(a[i] for i in range(n) if a[i] >= a[k - 1] and a[i] > 0))
