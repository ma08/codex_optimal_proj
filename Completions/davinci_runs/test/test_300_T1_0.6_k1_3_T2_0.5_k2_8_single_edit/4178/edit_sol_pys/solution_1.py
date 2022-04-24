

n = int(input())
a = list(map(int, input().split()))
if n == 1:
    print('Yes')
else:
    flag = True
    for i in range(1, n):
        if a[i] < a[i-1]:
            if a[i] < a[i-1] - 1:
                flag = False
                break
            else:
                a[i] = a[i-1]
    if flag:
        print('Yes')
    else:
        print('No')
