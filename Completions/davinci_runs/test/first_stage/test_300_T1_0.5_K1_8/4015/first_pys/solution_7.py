

n, m = [int(x) for x in input().split()]

if m % n != 0:
    print(-1)
else:
    count = 0
    while m > n:
        if m % 2 == 0:
            m /= 2
            count += 1
        elif m % 3 == 0:
            m /= 3
            count += 1
        else:
            print(-1)
            break
    if m == n:
        print(count)