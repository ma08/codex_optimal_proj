# AtCoder Beginner Contest 088 A - Infinite Coins
# https://atcoder.jp/contests/abc088/tasks/abc088_a 

K = int(input())
S = input()

if len(S) > K:
    print(S[:K] + '...')
else:
    print(S)
