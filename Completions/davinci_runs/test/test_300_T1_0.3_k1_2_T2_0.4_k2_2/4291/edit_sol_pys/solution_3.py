# https://atcoder.jp/contests/abc155/tasks/abc155_d
# D - Handshake
import bisect


n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

# create a list of the number of pairs
pairs = []
for i in range(n):
    for j in range(i+1, n):
        pairs.append(a[i] * a[j])
pairs.sort()

# find the kth largest pair
print(pairs[k-1])
