

n = int(input())
a = input().split(' ')

if len(a) != n:
    print('Something is fishy')
    flag = 0
else:
    for i in range(len(a)):
        if a[i] == 'mumble' or int(a[i]) == i+1:
            continue
        elif int(a[i]) != i+1:
            print('Something is fishy')
            flag = 1
            break;
    else:
        if flag == 0:
            print('makes sense')
