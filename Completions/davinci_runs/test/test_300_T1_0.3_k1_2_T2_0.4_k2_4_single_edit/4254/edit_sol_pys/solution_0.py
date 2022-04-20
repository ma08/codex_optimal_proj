

s, w = map(int, input().split())  # s: スピード w: 風速

if s <= w:
    print('unsafe')
else:
    print('safe')
