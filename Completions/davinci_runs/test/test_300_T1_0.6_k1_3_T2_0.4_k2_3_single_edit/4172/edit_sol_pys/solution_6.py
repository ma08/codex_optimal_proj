
# SOLUTION
a, b = map(int, input().split())

if a == b:
    print(0)
else:
    if a > b:
        print('>')
    elif a < b:
        print('<')
    else:
        print('=')
