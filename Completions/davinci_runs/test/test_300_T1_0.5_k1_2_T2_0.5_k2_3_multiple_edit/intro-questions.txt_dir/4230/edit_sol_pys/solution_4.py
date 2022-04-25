

x = int(input())
n = int(input())
p = list(map(int, input().split()))

p.sort()

if x < p[0]:  # если число меньше первого числа массива
    print(p[0] - x)
elif x > p[n-1]:  # если число больше последнего числа массива
    print(x - p[n-1])
else:  # иначе
    for i in range(1, n):
        if p[i-1] < x and x < p[i]:  # если число в промежутке между числами массива
            if abs(p[i-1] - x) < abs(p[i] - x):  # если модуль разности между числами массива и числом меньше
                print(p[i-1] - x)
            else:
                print(p[i] - x)
            break
