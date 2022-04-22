

N = int(input())

if N % 2 == 0:
    if N % 5 == 0:
        print('Yes')
    elif N % 3 == 0:
        print('Yes')
    else:
        print('No')
