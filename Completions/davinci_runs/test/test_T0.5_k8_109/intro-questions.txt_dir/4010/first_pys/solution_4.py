

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if n < 3:
        print('NO')
        continue
    if n == 3:
        if a[0] == a[1] or a[1] == a[2]:
            print('YES')
            continue
        else:
            print('NO')
            continue
    # n > 3    
    if a[0] == a[1]:
        i = 2
        while i < n:
            if a[0] == a[i]:
                print('YES')
                break
            i += 1
        if i == n:
            print('NO')
    else:
        if a[1] == a[2]:
            print('YES')
        else:
            print('NO')