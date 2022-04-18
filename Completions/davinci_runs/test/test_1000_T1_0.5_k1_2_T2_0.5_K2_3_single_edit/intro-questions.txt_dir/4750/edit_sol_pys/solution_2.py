
n = int(input())

for i in range(n):
    a = map(int, input().split())

    if a[0] == a[1]:
        print(a[0], a[2])
    elif a[2] == a[3]:
        print(a[0], a[2])
    elif a[0] == a[2]:
        print(a[0], a[1])
    elif a[1] == a[3]:
        print(a[0], a[1])
    elif a[0] == a[3]:
        print(a[0], a[2])
    elif a[1] == a[2]:
        print(a[0], a[1])
