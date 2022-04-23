

n = int(input())
h = list(map(int, input().split()))
if n == 1:
    print('Yes')
else:
    flag = True
    for i in range(1, n):
        if h[i] < h[i-1]:
            if h[i] < h[i-1] - 1:
                flag = False
                break
            else:
                h[i] = h[i-1]
    if flag:
        print('Yes')
    else:
        
        print('No')
