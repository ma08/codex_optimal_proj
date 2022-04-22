

n = int(input())

if n % 2 == 0 and n % 5 == 0:
    print('Yes')
elif n % 3 == 0 and n % 3 == 0:
    print('Yes')
elif n % 2 == 0 and n % 3 == 0:
    print('Yes')
else:
    print('No')
