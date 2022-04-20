
n = int(input())
h = list(map(int, input().split()))

if n == 1:
    print('Yes')
else:
    for i in range(n-1):
        if h[i] > h[i+1]:
            h[i] -= 1
            if h[i] > h[i+1]:
                print('No')
                exit()
    print('Yes')
