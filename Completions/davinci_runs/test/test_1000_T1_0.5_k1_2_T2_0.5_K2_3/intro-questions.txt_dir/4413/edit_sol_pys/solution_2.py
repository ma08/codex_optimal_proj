
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    if a[0]>=0:
        a.sort()
        ans = 1
        for i in range(1,n):
            if a[i]-a[i-1]==1:
                ans+=1
        print(ans)
    else:
        a.sort(reverse=True)
        ans = 1
        for i in range(1,n):
            if a[i]-a[i-1]==1:
                ans+=1
        print(ans)
