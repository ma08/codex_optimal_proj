
n = int(input())
a = list(map(int,input().split()))

ans = "YES"

for i in range(len(a)-1):
    if a[i] != a[i+1]:
        ans = "NO"
        break

print(ans)