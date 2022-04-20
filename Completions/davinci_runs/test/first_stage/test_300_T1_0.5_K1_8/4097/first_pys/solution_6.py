

n = int(input())
a = list(map(int, input().split()))

def check(a):
    if a[0] == a[-1]:
        return True
    return False

def check2(a):
    if a[0] > a[-1]:
        a[0], a[-1] = a[-1], a[0]
    if a[1] > a[0] + 1:
        a[1] = a[0] + 1
    elif a[1] < a[0] - 1:
        a[1] = a[0] - 1
    if a[1] == a[0]:
        return True
    if a[1] > a[-1]:
        return False
    d = a[1] - a[0]
    for i in range(2, n):
        if a[i] > a[i-1] + d:
            a[i] = a[i-1] + d
        elif a[i] < a[i-1] - d:
            a[i] = a[i-1] - d
        if a[i] == a[i-1]:
            return True
    return False

if n == 1:
    print(0)
elif n == 2:
    print(0)
else:
    if check(a):
        print(0)
    else:
        if check2(a):
            print(1)
        else:
            print(-1)