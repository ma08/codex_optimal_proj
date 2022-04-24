

n, m, c = map(int, input().split())
b = list(map(int, input().split()))
count = 0
for i in range(n):
  a = list(map(int, input().split()))
  if sum(map(lambda x, y:x*y, a, b)) + c > 0: #map(lambda x, y:x*y, a, b)はaとbの要素をそれぞれ掛けて返す。
    count += 1
print(count)
