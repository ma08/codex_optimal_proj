n, w = map(int, input().split())
a = list(map(int, input().split()))
print(w-abs(sum(a)) if sum(a) > w or sum(a) < -w or sum(a)+w < 0 or sum(a)-w > 0 else 0)
