
n, k = map(int, input().split())
a=list(map(int,input().split()))
a.sort()
if len(set(a)) < k:
    print("NO")
else:
    print("YES")
    for i in range(len(a)):
        if k == 0:
            break
        if i == 0:
            print(a[i], end=" ")
            k -= 1
        elif a[i] != a[i-1]:
            print(a[i], end=" ")
            k -= 1
