
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = []
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                d.append(j)
                break
    print(d)
    for i in range(n):
        for j in range(n):
            if j == d[i]:
                print(a[i], end=' ')
            else:
                print(b[j], end=' ')
        print()
