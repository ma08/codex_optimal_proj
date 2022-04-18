

t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            if l[i] == l[j]:
                print(l[i],end=" ")
                break
