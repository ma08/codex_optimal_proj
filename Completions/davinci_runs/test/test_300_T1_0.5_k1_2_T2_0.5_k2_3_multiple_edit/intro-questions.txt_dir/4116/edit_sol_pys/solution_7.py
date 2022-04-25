

n = int(input())
if n % 2 == 0 and n > 2 or n % 3 == 0 and n > 3 or n % 5 == 0 and n > 5 or n % 7 == 0 and n > 7:
    print('Yes')
else:
    print('No')
