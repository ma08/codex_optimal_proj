
#--------------------------------------------------------------------------------------------------------------------------
t = int(input())
for i in range(t):
    h, m = map(int, input().split())
    h = 24 - h
    if m != 0:
        h -= 1
        m = 60 - m
    else:
        h -= 1
    print(h*60 + m)


#--------------------------------------------------------------------------------------------------------------------------
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n):
        if arr[i] != i + 1:
            print(i + 1)
            break


#--------------------------------------------------------------------------------------------------------------------------
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n):
        if arr[i] != i + 1:
            print(i + 1)
            break


#--------------------------------------------------------------------------------------------------------------------------
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(n):
        if arr[i] != i + 1:
            print(i + 1)
            break
