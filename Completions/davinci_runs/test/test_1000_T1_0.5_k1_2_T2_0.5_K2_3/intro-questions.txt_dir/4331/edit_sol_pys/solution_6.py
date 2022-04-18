

n = int(input())

if n % 10 == 7:
    print('Yes')
elif n // 10 % 10 == 7:
    print('Yes')
elif n // 100 == 7:
    print('Yes')
else:

# fix syntax errors
    print('No')
