
for i in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    for j in range(n):
        for k in range(n):
            if (a[j]+b[k] < k):
                print("No")
                break
        else:
            continue
        break
    else:
        print("Yes")
