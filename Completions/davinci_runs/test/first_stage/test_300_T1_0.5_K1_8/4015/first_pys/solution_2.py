

n, m = map(int, input().split())

if n == m:
    print(0)
    exit()

answer = 0
while n != m:
    if m % 2 == 0 and m % 3 == 0:
        m //= 6
    elif m % 2 == 0:
        m //= 2
    elif m % 3 == 0:
        m //= 3
    else:
        print(-1)
        exit()
    answer += 1

print(answer)