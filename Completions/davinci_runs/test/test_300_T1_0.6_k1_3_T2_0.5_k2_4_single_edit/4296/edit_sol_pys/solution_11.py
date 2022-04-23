# https://atcoder.jp/contests/abc122/tasks/abc122_a

# My answer
a1, a2, a3 = map(int, input().split())
if a1 + a2 + a3 >= 22:
    print('bust')
else:
    print('win')
