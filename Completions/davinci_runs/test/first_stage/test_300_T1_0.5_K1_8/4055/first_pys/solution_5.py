

n = int(input())
a = [int(x) for x in input().split()]

if n <= 3:
    print(0)
else:
    c = 0
    for i in range(1, n-1):
        if a[i-1] == a[i+1] == 1 and a[i] == 0:
            c += 1
    print(c)