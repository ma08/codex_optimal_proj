
# https://atcoder.jp/contests/abc081/tasks/arc086_a
import math

n, k = map(int, input().split())

a = list(map(int, input().split()))

counts = {}
for ai in a:
    if ai in counts:
        counts[ai] += 1
    else:
        counts[ai] = 1

counts = sorted(counts.items(), key=lambda x: x[1])

remove_count = 0
for i in range(len(counts) - k):
    remove_count += counts[i][1]

print(remove_count)
