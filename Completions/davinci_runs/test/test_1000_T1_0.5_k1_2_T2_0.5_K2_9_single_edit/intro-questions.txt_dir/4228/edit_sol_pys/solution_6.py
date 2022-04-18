# https://atcoder.jp/contests/abc082/tasks/abc082_b

n, l = map(int, input().split())

flavors = [l + i for i in range(n)]

print(sum(flavors) - min(flavors, key=lambda x: abs(x)))
