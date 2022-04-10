
n, m = map(int, input().split())

if n == m:
    print(0)
    exit()

if m % n:
    print(-1)
    exit()

count = 0
while m != n:
    if m % 2 and m % 3:
        print(-1)
        exit()
    elif m % 2 == 0:
        m //= 2
    else:
        m //= 3
    count += 1

print(count)
