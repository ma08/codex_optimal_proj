# AtCoder Beginner Contest 069
# A - 何個でも足せるよ
# https://atcoder.jp/contests/abc069/tasks/abc069_a

D, N = map(int, input().split())

if D == 0:
    print(N)
elif D == 1:
    print(100 * N)
else:
    print(10000 * N)
