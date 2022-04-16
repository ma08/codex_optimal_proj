

n = int(input())
a = input().split()

if len(a) != n:
    print('Something is fishy')
else:
    for i in range(len(a)):
        if a[i] == 'mumble':
            continue
        elif int(a[i]) == i+1:
            continue
        else:
            print('Something is fishy')
            break
    else:
        print('Makes sense')
