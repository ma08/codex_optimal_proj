
# SOLUTION
for _ in range(int(input())):
    n = int(input())
    d = list(map(int, input().split()))
    d.sort()
    if n == 1:
        x = d[0] * 2
    elif n == 2:
        x = d[0] * d[1]
    elif n == 3:
        if d[1] % d[0] == 0:
            x = d[1]
        else:
            x = -1
    else:
        x = -1
    print(x)