# A - B+C
# https://atcoder.jp/contests/abc086/tasks/abc086_a

n, m, c = map(int, input().split())
b = list(map(int, input().split()))
count = 0
for i in range(n):
  a = list(map(int, input().split()))
  if sum(map(lambda x, y:x*y, a, b)) + c > 0:
    count += 1
print(count)
