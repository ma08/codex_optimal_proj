

x, a, b = map(int, input().split())

if b >= 0:
    if x >= a:
        print('delicious')
    elif x >= a - b:
        print('safe')
    else:
        print('dangerous')
else:
    print('dangerous')
