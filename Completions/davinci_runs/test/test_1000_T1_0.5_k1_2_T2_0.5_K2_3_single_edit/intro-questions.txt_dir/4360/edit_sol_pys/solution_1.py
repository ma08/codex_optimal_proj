# https://atcoder.jp/contests/abc125/tasks/abc125_a

n = int(input())
a = list(map(int, input().split()))

a_sum = 0
for i in range(n):
    a_sum += 1/a[i]

print(1/a_sum)
