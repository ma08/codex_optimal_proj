# https://atcoder.jp/contests/abc135/tasks/abc135_c
# https://atcoder.jp/contests/abc135/submissions/13179465


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a = [1, 2, 3]
# b = [2, 1, 3]

a.sort()
b.sort()

min_cost = float('inf')
for i in range(n):
    cost = 0
    for j in range(n):
        cost += abs(b[j] - a[i])
    min_cost = min(min_cost, cost)

print(min_cost)
