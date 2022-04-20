
# My answer
a1, a2, a3 = map(int, input().split())
if a1 + a2 + a3 >= 22:
    print('bust')
else:

# My answer
a, b = map(int, input().split())
if a == b:
    print('Draw')
elif a == 1:
    print('Alice')
elif b == 1:
    print('Bob')
elif a > b:
    print('Alice')
else:
    print('Bob')
    print('win')
