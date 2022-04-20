

n = int(input())

if n % 4 == 0 or n % 7 == 0:
    print('Yes')
elif n > 7:
    for i in range(n//7):
        if (n - 7 * i) % 4 == 0:
            print('Yes')
            break
    else:
        print('No')
else:
    print('No')