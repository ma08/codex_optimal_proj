n, w = map(int, input().split())
a = list(map(int, input().split()))
print(w - abs(sum(a)))
