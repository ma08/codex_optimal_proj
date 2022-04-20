

s, w = map(int, input().split())  # s: 強さ, w: 重さ

if s <= w:
    print('unsafe')
else:
    print('safe')
