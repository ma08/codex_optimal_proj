

n = int(input())
a = [int(i) for i in input().split()]

if n == 2:
    print(abs(a[0] - a[1]))
else:
    max_a = max(a)
    min_a = min(a)
    if max_a == min_a:
        print(0)
    else:
        if max_a % min_a == 0:
            print(max_a - min_a)
        else:
            print(-1)