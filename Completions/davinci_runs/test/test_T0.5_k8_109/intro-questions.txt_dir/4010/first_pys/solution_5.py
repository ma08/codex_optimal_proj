

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    flag = False
    for i in range(n-2):
        if a[i] == a[i+1]:
            if a[i+1] == a[i+2]:
                flag = True
                break
            if i+3 < n and a[i+1] == a[i+3]:
                flag = True
                break
    if flag:
        print("YES")
    else:
        print("NO")