
n = int(input())
a = list(map(int,input().split()))

#n = int(input())
#a = [int(i) for i in input().split()]

#print(n)
#print(a)

ma = []
ma.append(0)
ma.append(1)

for i in range(1,n):
    if a[i] > a[i-1]:
        ma.append(ma[i]+1)
    else:
        ma.append(1)

print(ma)

mb = []
mb.append(0)
mb.append(1)

for i in range(1,n):
    if a[n-1-i] < a[n-i]:
        mb.append(mb[i]+1)
    else:
        mb.append(1)

print(mb)

mb.reverse()

print(mb)

m = 0

for i in range(1,n+1):
    m = max(m,ma[i-1] + mb[i]-1)

print(m)
