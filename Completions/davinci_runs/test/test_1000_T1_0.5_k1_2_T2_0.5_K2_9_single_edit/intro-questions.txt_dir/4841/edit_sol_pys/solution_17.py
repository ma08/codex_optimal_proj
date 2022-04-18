

n = int(input())
a = list(map(int, input().split()))

if len(a) != n:
    print('something is fishy')
else:
    for i in range(len(a)):
        if a[i] == i+1:
            continue
        else:
            print('something is fishy')
            break
    else:
        print('makes sense')
