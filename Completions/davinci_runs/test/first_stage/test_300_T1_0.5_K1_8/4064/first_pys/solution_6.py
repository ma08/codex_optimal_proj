

# Solution

#1st solution
n,h,l,r = map(int,input().split())
a = list(map(int,input().split()))

cnt = 0
for i in range(n):
   if l <= (a[i]-1)%h <= r:
      cnt += 1
   elif l <= a[i]%h <= r:
      cnt += 1
print(cnt)

#2nd solution
n,h,l,r = map(int,input().split())
a = list(map(int,input().split()))

cnt = 0
for i in range(n):
   if l <= (a[i]-1)%h <= r or l <= a[i]%h <= r:
      cnt += 1
print(cnt)