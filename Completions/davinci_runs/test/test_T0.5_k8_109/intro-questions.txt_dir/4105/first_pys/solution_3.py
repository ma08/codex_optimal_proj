

n, k = map(int, input().split())

if n == 1:
    print("YES")
    print(1, 2)
elif k == 1:
    print("NO")
elif k == 2:
    print("YES")
    for i in range(1, n):
        print(i, i+1)
        i += 1
    print(n, 1)
else:
    print("YES")
    for i in range(1, n):
        if i%2 == 0:
            print(i, i+1)
            i += 1
        else:
            print(i+1, i)
            i += 1
    print(n, 1)