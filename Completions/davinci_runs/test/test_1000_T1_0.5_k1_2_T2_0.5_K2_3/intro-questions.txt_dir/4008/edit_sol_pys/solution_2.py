

n, k = map(int, input().split())
a = list(map(int, input().split()))
if n == 1:
    print("Yes")
    print(1)
else:
    b = [0]*n
    if a[0] in a[1:]:
        print("No")
    else:
        for i in range(n):
            if a[i] == a[0]:
                b[i] = 1
            else:
                b[i] = 2
        print("Yes")
        print(*b)
