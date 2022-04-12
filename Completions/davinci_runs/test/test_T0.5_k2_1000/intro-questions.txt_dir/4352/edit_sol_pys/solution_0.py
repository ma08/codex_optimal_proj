a, b = map(int, input().split())

if a == 1:
    if b == 1:
        print('Draw')
    else:
        print('Alice')
elif b == 1:
    print('Bob')
else:
    if a > b:
        print('Alice')
    elif a < b:
        print('Bob')
    else:
        print('Draw')
