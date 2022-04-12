
# https://atcoder.jp/contests/abc085/tasks/abc085_b
c, k = map(int, input().split())

if c % 10**k >= 5*10**(k-1):
    print(c + (10**k - c % 10**k))
else:
    print(c - c % 10**k)
