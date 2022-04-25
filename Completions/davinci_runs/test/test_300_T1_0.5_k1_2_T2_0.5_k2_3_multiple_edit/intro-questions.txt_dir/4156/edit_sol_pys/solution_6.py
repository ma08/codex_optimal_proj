n, w = map(int, input().split())
a = list(map(int, input().split()))
print(max(0, w - abs(sum(a))))
