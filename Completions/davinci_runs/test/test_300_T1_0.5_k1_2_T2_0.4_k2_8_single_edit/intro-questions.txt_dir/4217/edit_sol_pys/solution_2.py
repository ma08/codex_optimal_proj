# https://atcoder.jp/contests/abc086/tasks/abc086_a


a, b = map(int, input().split())

if a * b % 2 == 0:
    print('Even')
else:
    print('Odd')
