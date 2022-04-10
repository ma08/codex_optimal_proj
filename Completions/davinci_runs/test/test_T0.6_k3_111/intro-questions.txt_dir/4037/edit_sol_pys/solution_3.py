
# https://codeforces.com/contest/1253/problem/B
n,r = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
a.sort(key=lambda x:x[0])
#print(a)
result = 0
for i in range(n):
    if a[i][0]<=r:
        result+=1
        r+=a[i][1]
    else:
        break
print(result)
