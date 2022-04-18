while True:
    n = int(input())
    if n == 0:
        break
    else:
        a = list(map(int, input().split()))
        a.sort()
        for i in range(n):
            print(a[i], end=" ")
        print()
