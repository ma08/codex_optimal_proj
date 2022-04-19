# https://codeforces.com/contest/1272/problem/A

n, k = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]

print(max(a) - min(a) - (k - 1))
