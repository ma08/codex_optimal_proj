

# My answer
a1, a2, a3 = map(int, input().split())   # inputを空白で分けてint型に変換
if a1 + a2 + a3 >= 22:
    print('bust')
else:
    print('win')
