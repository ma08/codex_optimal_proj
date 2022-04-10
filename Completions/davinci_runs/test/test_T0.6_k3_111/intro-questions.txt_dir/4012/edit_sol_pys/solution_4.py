
# Solution 1 (wrong)

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    count = 0
    while True:
        if b % a == 0 and c % b == 0:
            print(count)
            print(a, b, c)
            break
        if a > b:
            b += 1
            count += 1
        elif b > c:
            c += 1
            count += 1
        elif a == b:
            a += 1
            count += 1

# Solution 2 (wrong)

t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    count = 0
    if b % a == 0 and c % b == 0:
        print(count)
        print(a, b, c)
        continue
    if a > b:
        b += 1
        count += 1
    elif b > c:
        c += 1
        count += 1
    elif a == b:
        a += 1
        count += 1
    print(count)
    print(a, b, c)
