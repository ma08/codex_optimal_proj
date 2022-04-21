

n, k = list(map(int, input().split()))
a = list(map(int, input().split()))

print(max(a) if k == 1 else max(a) - min(a) + 1)
