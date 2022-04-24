

n = int(input())
x = [int(i) for i in input().split()]

if n == 1:
    print(0, end='')
else:
    x.sort()
    if x[0] == x[-1]:
        print(0, end='')
    else:
        if x[1] == x[-1]:
            print(x[-1] - x[1], end='')
        else:
            print(min(x[-1] - x[1], x[-2] - x[0]), end='')
