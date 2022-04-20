

#Solution

n = int(input())
a = list(map(int,input().split()))

for i in range(n):
    for j in range(i+1,n):
        if abs(a[i]-a[j])>=2:
            print("NO")
            exit()
print("YES")