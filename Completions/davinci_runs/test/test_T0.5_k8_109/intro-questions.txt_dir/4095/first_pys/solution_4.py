

#submitted by thr3sh0ld
#programming language: Python3

n, m = map(int,input().split())
a = list(map(int,input().split()))
b = [0]*n
c = [0]*n
for i in range(n):
    b[i] = a[i]
    c[i] = a[i]
b.sort()
c.sort()
c.reverse()
ans = 0
for i in range(n):
    if(b[i]==m):
        ans += i
    if(c[i]==m):
        ans += i
print(ans)