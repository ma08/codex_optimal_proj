

n = int(input())
b = list(map(int,input().split()))
b.sort()
if n == 2:
    print(b[0]+b[1])
elif n == 1:
    print(b[0])
else:
    a = [0] * n
    for i in range(n-1):
        # print(i)
        if i == 0:
            a[i] = b[i] - b[i+1] + b[i+2]
            a[i+1] = b[i+1] - b[i] + b[i+2]
            a[i+2] = b[i+2] - b[i] - b[i+1]
        else:
            a[i] = b[i] - b[i-1] - a[i-1]
            a[i+1] = b[i+1] - b[i-1] - a[i-1]
    print(sum(a))