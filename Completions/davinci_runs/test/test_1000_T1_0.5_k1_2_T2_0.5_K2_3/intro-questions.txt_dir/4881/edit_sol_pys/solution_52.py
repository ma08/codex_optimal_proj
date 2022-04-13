

n = int(input())

if n % 2 == 0 and n > 0:
    print('Even')
elif n % 2 == 1 and n > 0:
elif n < 0:
    print('invalid')
    print('Odd')
else:
    print('Either odd or even')
