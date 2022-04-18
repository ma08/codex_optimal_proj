t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    for j in a:
        print(j,end=" ")
    print()
