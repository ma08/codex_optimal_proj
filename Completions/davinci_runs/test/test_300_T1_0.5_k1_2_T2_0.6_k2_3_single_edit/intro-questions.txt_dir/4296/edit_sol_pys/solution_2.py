

a1, a2, a3 = map(int, input().split())
if a1+a2+a3 >= 22 and a1 == 11:
    if a1+a2+a3-10 >= 22:
        print('bust')
    else:
        print('win')
elif a1+a2+a3 >= 22 and a2 == 11:
    if a1+a2+a3-10 >= 22:
        print('bust')
    else:
        print('win')
elif a1+a2+a3 >= 22 and a3 == 11:
    if a1+a2+a3-10 >= 22:
        print('bust')
    else:
        print('win')
elif a1+a2+a3 >= 22 and a1 == 11 and a2 == 11:
    if a1+a2+a3-20 >= 22:
        print('bust')
    else:
        print('win')
elif a1+a2+a3 >= 22 and a1 == 11 and a3 == 11:
    if a1+a2+a3-20 >= 22:
        print('bust')
    else:
        print('win')
elif a1+a2+a3 >= 22 and a1 == 11 and a3 == 11:
    if a1+a2+a3-20 >= 22:
        print('bust')
    else:
        print('win')
elif a1+a2+a3 >= 22 and a1 == 11 and a2 == 11 and a3 == 11:
    if a1+a2+a3-30 >= 22:
        print('bust')
    else:
        print('win')
else:
    print('win')
