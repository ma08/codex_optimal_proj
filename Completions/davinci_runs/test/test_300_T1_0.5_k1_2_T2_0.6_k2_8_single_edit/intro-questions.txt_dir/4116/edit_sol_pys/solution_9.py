

N = int(input())

if N % 2 == 0 or N % 5 == 0:
    if N % 3 == 0 or N % 3 == 0:
        if N % 2 == 0 or N % 3 == 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')
