
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    a.sort()
    print(a[k-1])
