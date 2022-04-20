

n = int(input())

if n == 7 or n == 4 or n == 11:
    print('Yes')
elif n > 11:
    if n % 4 == 0:
        print('Yes')
    elif n % 7 == 0:
        print('Yes')
    elif n % 4 == 3 and n > 14:
        print('Yes')
    elif n % 7 == 3 and n > 11:
        print('Yes')
    else:
        print('No')
else:
    print('No')