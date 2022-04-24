
n, m = map(int, input().split())

if n == m:
    print(0)
    quit()

steps = 0

while n != m:
    if n % 3 == 0:
        n = int(n / 3)
    elif n % 2 == 0:
        n = int(n / 2)
    else:
        print(-1)
        quit()
    steps += 1

print(steps)
