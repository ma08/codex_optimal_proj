

n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        print(' {}'.format(i), end='')
    else:
        a = i
        while a != 0:
            if a % 10 == 3:
                print(' {}'.format(i), end='')
                break
            a //= 10
